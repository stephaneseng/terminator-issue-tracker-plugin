#!/usr/bin/env python2

import re
import terminatorlib.plugin as plugin

AVAILABLE = ['IssueTrackerURLHandler']

PROJECT_KEYS_TO_URL_PATTERNS = {
    'JIRA_PROJECT_KEY': 'https://JIRA_INSTANCE.atlassian.net/browse/{project}-{id}',
    'REDMINE': 'https://REDMINE_URL/issues/{id}'
}


class IssueTrackerURLHandler(plugin.URLHandler):
    capabilities = ['url_handler']
    handler_name = 'issue_tracker_url_handler'
    match = r'\b(?P<project>{projects})-(?P<id>[0-9]+)\b'.format(projects='(' + '|'.join(list(PROJECT_KEYS_TO_URL_PATTERNS.keys())) + ')')

    def callback(self, url):
        m = re.match(self.match, url)
        project = m.group('project')
        id_ = m.group('id')
        return PROJECT_KEYS_TO_URL_PATTERNS[project].format(project=project, id=id_)
