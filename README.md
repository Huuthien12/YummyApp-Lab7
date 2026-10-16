# YummyApp Lab 7 - Software Testing

Student: Luong Huu Thien | MSSV: 2312753

## Run on Python 3.11

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
coverage run --source=gps_service,yummy_app -m unittest discover -s . -p "test_*.py"
coverage report -m
coverage html -d coverage_html
coverage report --fail-under=80
```

Push the repository to GitHub main to execute the workflow. To demonstrate red/green CI, make separate commits for the initial 4 tests, quality gate (red), completed tests (green), temporary syntax error (red), and correction (green). **Do not submit fabricated logs.** Download raw GitHub Actions logs after a real run and save as `logs/github_actions_run.log`. Create `logs/git_history.log` from real repository commits. Handwrite and sign the required 4 pages and scan them into `MinhChung_VietTay_2312753.pdf`. Add GitHub URL and screenshots to report.
