"""
Writing tests for the commit-msg.py git hook.
"""

__author__ = 'ameadows'

import unittest
import os
import subprocess

class CommitMessageTests(unittest.TestCase):

    def setUp(self):
        self.test_files_loc = "./test_files/"

    def testGoodMessage(self):
        expected_result = ''

        given_result = subprocess.check_output(args=["../client/commit-msg.py", "./test_files/message_file_good.txt"])

        self.assertEqual(given_result, expected_result)

    def testBadSubjectLine(self):
        expected_result = ''
        
        given_result = subprocess.check_output(args=["../client/commit-msg.py", "./test_files/message_file_bad.txt"])

        self.assertEqual(given_result, expected_result)

    # def testEmptySubjectLine(self):
    #
    # def testBadMessage(self):
    #
    # def testEmptyMessage(self):
    #
    # def testEmptyBreak(self):
    #
    # def testBadBreak(self):
    #
    # def testBadStory(self):
    #
    # def testEmptyStory(self):
    #
    #
    #
