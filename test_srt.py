# -*- coding: UTF-8 -*-
import unittest
from srt import *

class srtTests(unittest.TestCase):
    def test_valid_period(self):
        period = '00:00:27,210 --> 00:00:31,680'
        self.assertTrue(is_period(period))
        period_with_spaces = '  00:00:27,210  --> 00:00:31,680  '
        self.assertTrue(is_period(period))

    def test_invalid_period(self):
        period = '00:00:27,210 --> '
        self.assertFalse(is_period(period))
        period = '--> 00:00:31,680'
        self.assertFalse(is_period(period))

    def test_parse_one_subtitle(self):
        serial = '1'
        period = '00:00:27,210 --> 00:00:31,680'
        content = '停下-啊!'
        text = '\n'.join([serial, period, content])
        srt = parse(text)
        self.assertEqual(1, len(srt.subtitles))
        self.assertEqual(serial, srt.subtitles[0].serial)
        self.assertEqual(period, srt.subtitles[0].period)
        self.assertEqual(content, srt.subtitles[0].content)

    def test_parse_subtitles(self):
        serial = '1'
        period = '00:00:27,210 --> 00:00:31,680'
        content = '停下-啊!'
        subtitle = '\n'.join([serial, period, content])
        subtitles = '\n'.join([subtitle, subtitle, subtitle])
        srt = parse(subtitles)
        self.assertEqual(3, len(srt.subtitles))

    def test_parse_subtitles_with_random_title(self):
        text = """
            ABC

            1
            00:00:27,210 --> 00:00:31,680
            停下-啊!

            2
            00:00:37,050 --> 00:00:40,850
            燈光"""
        srt = parse(text)
        self.assertEqual(2, len(srt.subtitles))
        self.assertEqual('1', srt.subtitles[0].serial)
        self.assertEqual('00:00:27,210 --> 00:00:31,680', srt.subtitles[0].period)
        self.assertEqual('停下-啊!', srt.subtitles[0].content)
        self.assertEqual('2', srt.subtitles[1].serial)
        self.assertEqual('00:00:37,050 --> 00:00:40,850', srt.subtitles[1].period)
        self.assertEqual('燈光', srt.subtitles[1].content)

    def test_parse_subtitles_with_missing_serial_number(self):
        text = """
            00:00:27,210 --> 00:00:31,680
            停下-啊!

            1
            00:00:37,050 --> 00:00:40,850
            燈光"""
        srt = parse(text)
        self.assertEqual(2, len(srt.subtitles))
        self.assertEqual('1', srt.subtitles[0].serial)
        self.assertEqual('00:00:27,210 --> 00:00:31,680', srt.subtitles[0].period)
        self.assertEqual('停下-啊!', srt.subtitles[0].content)
        self.assertEqual('2', srt.subtitles[1].serial)
        self.assertEqual('00:00:37,050 --> 00:00:40,850', srt.subtitles[1].period)
        self.assertEqual('燈光', srt.subtitles[1].content)



if __name__ == '__main__':
    unittest.main()
