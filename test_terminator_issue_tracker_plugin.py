#!/usr/bin/env python2

import unittest
from parameterized import parameterized
from terminator_issue_tracker_plugin import IssueTrackerURLHandler


class TestIssueTrackerURLHandler(unittest.TestCase):

    def setUp(self):
        self.issue_tracker_url_handler = IssueTrackerURLHandler()

    @parameterized.expand([
        ('JIRA_PROJECT_KEY-1', 'https://JIRA_INSTANCE.atlassian.net/browse/JIRA_PROJECT_KEY-1'),
        ('REDMINE-2', 'https://REDMINE_URL/issues/2')
    ])
    def test_test(self, key, expected):
        self.assertEqual(expected, self.issue_tracker_url_handler.callback(key))


if __name__ == '__main__':
    unittest.main()
