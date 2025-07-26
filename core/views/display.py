from rich.console import Console

console = Console()

def print_response(text):
    console.print("\n[bold green]ChatGPT:[/bold green]", text)