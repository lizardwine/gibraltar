import rich

def pytest_output(args):
    
    failed = 0
    passed = 0
    ignored = 0
    
    for group in args.groups:
        group_name = group["name"]
        group_name = group_name.replace("-", " ").replace("_", " ")
        group_name = group_name.title()
        passed_tests = len([test for test in group["tests"] if test.get('status', {'passed': False}).get('passed')])
        not_passed_tests = len([test for test in group["tests"] if not test.get('status', {'passed': True}).get('passed')])
        ignored = len([test for test in group["tests"] if test.get("ignore")])
        rich.print(f"[bold cyan]{group['file']}[/bold cyan]  [bold green]{'✓'*passed_tests}[/bold green][bold yellow]{'~'*ignored}[/bold yellow][bold red]{'✗'*not_passed_tests}[/bold red]")
        failed += not_passed_tests
        passed += passed_tests
        ignored += ignored
    if passed > 0:
        rich.print(f"[bold green]{passed} passed tests[/bold green]")
    if ignored > 0:
        rich.print(f"[bold yellow]{ignored} ignored tests[/bold yellow]")
    if failed > 0:
        rich.print(f"[bold red]{failed} failed tests[/bold red]")

litio = {
    'output': {
        'pytest': pytest_output
    }
}