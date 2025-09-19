import time
import argparse
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.panel import Panel

console = Console()

def timer(total_seconds):
    with Progress(
        TextColumn("[bold]⏳ Progress session"),
        BarColumn(bar_width=50, complete_style="blue"),
        TextColumn("[bold]{task.description}", justify="left"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("⏳ Time remaining", total=total_seconds)
        while total_seconds:
            total_seconds -= 1
            hour = total_seconds // 3600
            minute = (total_seconds % 3600) // 60
            seconde = total_seconds % 60
            progress.update(task, advance=1, description=f"{hour:02}:{minute:02}:{seconde:02}")
            time.sleep(1)

def rule(time, session, pause):
    console.print(Panel(f"📅 Number of session : [bold red]{session}[/bold red] \n🕓 Session Duration : [bold red]{time}[/bold red] minute(s) \n🎉 Pause Duration [bold red]{pause}[/bold red] minute(s)\n\n👊 [bold green]Never Give UP ![/bold green]",expand=False,border_style="blue"))
    for i in range(1, session + 1):
        console.print(Panel(f"⏱️  [bold blue]Session n°{i}/{session} [/bold blue]",expand=False,border_style="blue"))
        session_minute = time
        total_seconds = session_minute * 60
        timer(total_seconds)
        console.print(f"[bold green]Session n°{i} finished ! Yay 🎉[/bold green]")
        
        if i != session:
            console.print(Panel(f"[bold green]Pause... 🏖️ [/bold green]",expand=False,border_style="green"))
            pause_minute = pause
            total_seconds = pause_minute * 60
            timer(total_seconds)

def main():
    parser = argparse.ArgumentParser(description='Simple CLI pomdoro')
    parser.add_argument('-t', '--time', default=25, help="Define the duration of the work session (in min)")
    parser.add_argument('-s', '--session', default=1, help="Define the number of work sessions")
    parser.add_argument('-p', '--pause', default=5, help="Define the break time between each work session (in min)")
    args = vars(parser.parse_args())
    rule(int(args["time"]),int(args["session"]), int(args["pause"]))
    console.print(f"[bold green]Session finished ! Good Job 🎉[/bold green]")

main()



