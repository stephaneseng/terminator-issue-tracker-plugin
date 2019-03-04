# terminator-issue-tracker-plugin

A [Terminator](https://gnometerminator.blogspot.com/p/introduction.html) plugin, transforming JIRA Issue Keys into clickable links.

## Configuration and installation

1. Customize the dictionary of Issue Keys to URL patterns in `terminator_issue_tracker_plugin.py`

2. Copy your modified `terminator_issue_tracker_plugin.py` file into your `~/.config/terminator/plugins/` folder.

    ```
    mkdir -p ~/.config/terminator/plugins/
    cp terminator_issue_tracker_plugin.py ~/.config/terminator/plugins/
    ```

3. In Terminator, enable the `IssueTrackerURLHandler` plugin, now listed in the Plugins list (Preferences > Plugins).

## Development

### Run the tests

```
(venv) $ pip install -r requirements.txt
(venv) $ python -m unittest test_terminator_issue_tracker_plugin
```
