from time import sleep

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import BarColumn, Progress, TextColumn
from rich.table import Table
from rich.text import Text


console = Console()


def _score_bar(score, bar_width=24):
    progress = Progress(
        TextColumn("[bold green]Score[/bold green]"),
        BarColumn(bar_width=bar_width, complete_style="green", finished_style="green"),
        TextColumn(f"[bold white]{score}/100[/bold white]"),
        expand=False,
    )
    progress.add_task("score", total=100, completed=score)
    return progress


def clear_screen():
    console.clear()


def welcome_screen():
    title = Text("NUMBER GUESSING GAME", style="bold white")
    subtitle = Text("Smart hints | Scores | Leaderboard", style="cyan")
    console.print(
        Panel(
            Text.assemble(title, "\n", subtitle, justify="center"),
            border_style="cyan",
            box=box.DOUBLE,
            padding=(1, 4),
        )
    )


def show_best_score(best_score):
    console.print(f"[bold cyan]Best Score[/bold cyan] : [bold green]{best_score}[/bold green]")


def show_menu():
    table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan")
    table.add_column("Option", justify="center", style="bold white", width=8)
    table.add_column("Mode", style="bold")
    table.add_column("Range", justify="center")
    table.add_column("Lives", justify="center")

    table.add_row("1", "[green]Easy[/green]", "1 - 20", "8")
    table.add_row("2", "[yellow]Medium[/yellow]", "1 - 50", "6")
    table.add_row("3", "[red]Hard[/red]", "1 - 100", "5")
    table.add_row("4", "[cyan]View Statistics[/cyan]", "-", "-")
    table.add_row("5", "[cyan]View Leaderboard[/cyan]", "-", "-")
    table.add_row("6", "[magenta]Reset Scores[/magenta]", "-", "-")
    table.add_row("7", "Exit", "-", "-")

    console.print(table)


def show_difficulty_info(difficulty):
    mode_style = {
        "Easy": "green",
        "Medium": "yellow",
        "Hard": "red",
    }.get(difficulty.name, "white")

    table = Table(box=box.SIMPLE_HEAVY, show_header=False, expand=True)
    table.add_column("Label", style="bold cyan", width=14)
    table.add_column("Value", style="white")
    table.add_row("Difficulty", f"[bold {mode_style}]{difficulty.name}[/bold {mode_style}]")
    table.add_row("Range", f"{difficulty.minimum} - {difficulty.maximum}")
    table.add_row("Lives", f"[red]{'♥' * difficulty.lives}[/red]")
    table.add_row("Goal", "Guess the hidden number before lives run out")
    console.print(Panel(table, title="GAME SETUP", border_style=mode_style, box=box.DOUBLE))


def show_game_status(lives, guess_no, score, history, elapsed_seconds):
    table = Table(box=box.SIMPLE_HEAVY, show_header=False, expand=True)
    table.add_column("Metric", style="bold cyan", width=14)
    table.add_column("Value", style="white")
    table.add_row("Lives Left", f"[red]{lives}[/red]")
    table.add_row("Guess No.", f"[bold yellow]{guess_no}[/bold yellow]")
    table.add_row("Score", _score_bar(score, bar_width=12))
    table.add_row("Timer", f"[cyan]{elapsed_seconds:.1f}s[/cyan]")
    if history:
        recent = ", ".join(str(guess) for guess in history[-8:])
        if len(history) > 8:
            recent = f"... {recent}"
        table.add_row("Previous", f"[magenta]{recent}[/magenta]")
    else:
        table.add_row("Previous", "[dim]No guesses yet[/dim]")
    console.print(Panel(table, title="CURRENT ROUND", border_style="cyan", box=box.DOUBLE))


def ask_choice(prompt):
    return console.input(f"[bold white]{prompt}[/bold white]").strip()


def ask_int(prompt):
    value = console.input(f"[bold white]{prompt}[/bold white]").strip()
    try:
        return int(value)
    except ValueError:
        return None


def show_hint(hint):
    icons = {
        "Very Close!": "\U0001f525",
        "Much Lower": "\U0001f4c9",
        "Much Higher": "\U0001f4c8",
        "Too Low": "\u2b07\ufe0f",
        "Too High": "\u2b06\ufe0f",
        "Correct!": "\u2705",
    }
    styles = {
        "Very Close!": "bold yellow",
        "Much Lower": "bold red",
        "Much Higher": "bold red",
        "Too Low": "bold cyan",
        "Too High": "bold cyan",
        "Correct!": "bold green",
    }
    icon = icons.get(hint, "\U0001f4a1")
    style = styles.get(hint, "bold white")
    console.print(
        Panel(
            f"{icon} [{style}]{hint}[/{style}]",
            title="HINT",
            border_style="yellow",
            box=box.ROUNDED,
            padding=(1, 3),
        )
    )


def show_win_screen(player_name, secret_number, attempts, score, difficulty, elapsed_seconds):
    table = Table.grid(padding=(0, 2))
    table.add_column(style="bold cyan", width=17)
    table.add_column(style="white")
    table.add_row("Player          :", f"[bold]{player_name}[/bold]")
    table.add_row("Correct Number  :", f"[bold green]{secret_number}[/bold green]")
    table.add_row("Attempts        :", str(attempts))
    table.add_row("Final Score     :", f"[bold green]{score}/100[/bold green]")
    table.add_row("Difficulty      :", difficulty)
    table.add_row("Time            :", f"{elapsed_seconds:.1f}s")
    console.print(
        Panel(
            table,
            title="YOU WIN",
            subtitle=f"Score saved | {score} points",
            border_style="green",
            box=box.DOUBLE,
            expand=False,
        )
    )


def show_lose_screen(secret_number):
    table = Table.grid(padding=(0, 2))
    table.add_column(style="bold cyan", width=17)
    table.add_column(style="white")
    table.add_row("Correct Answer  :", f"[bold red]{secret_number}[/bold red]")
    table.add_row("Result          :", "[bold red]No lives left[/bold red]")
    table.add_row("Message         :", "[yellow]Better Luck Next Time[/yellow]")
    console.print(
        Panel(
            table,
            title="GAME OVER",
            subtitle="Try again and beat the number",
            border_style="red",
            box=box.DOUBLE,
            expand=False,
        )
    )


def show_statistics(stats):
    table = Table(box=box.ROUNDED, show_header=False)
    table.add_column("Category", style="bold white", width=18)
    table.add_column("Result", justify="right", width=12)
    table.add_row("Games Played", f"[cyan]{stats['games_played']}[/cyan]")
    table.add_row("Games Won", f"[green]{stats['games_won']}[/green]")
    table.add_row("Games Lost", f"[red]{stats['games_lost']}[/red]")
    table.add_row("Win Rate", f"[yellow]{stats['win_rate']}%[/yellow]")
    table.add_row("Best Score", f"[green]{stats['best_score']}[/green]")
    table.add_row("Average Guesses", f"[cyan]{stats['average_guesses']}[/cyan]")
    console.print(
        Panel(
            table,
            title="STATISTICS",
            border_style="cyan",
            box=box.DOUBLE,
            expand=False,
        )
    )


def show_leaderboard(scores):
    if not scores:
        console.print(
            Panel(
                "[dim]No winning scores yet. Win a round to appear here.[/dim]",
                title="LEADERBOARD",
                border_style="cyan",
                box=box.DOUBLE,
                expand=False,
            )
        )
        return

    table = Table(box=box.ROUNDED, header_style="bold cyan", padding=(0, 1))
    table.add_column("Rank", justify="center", width=5)
    table.add_column("Player", width=16, no_wrap=True)
    table.add_column("Score", justify="right", style="bold green", width=7)
    table.add_column("Mode", justify="center", width=8)
    table.add_column("Guesses", justify="right", width=7)

    for index, score in enumerate(scores, start=1):
        medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(index, str(index))
        mode_style = {
            "Easy": "green",
            "Medium": "yellow",
            "Hard": "red",
        }.get(score["difficulty"], "white")
        table.add_row(
            medal,
            score.get("player_name", "Player")[:16],
            str(score["score"]),
            f"[{mode_style}]{score['difficulty']}[/{mode_style}]",
            str(score["guesses"]),
        )
    console.print(
        Panel(
            table,
            title="LEADERBOARD",
            subtitle="Top 10 winning scores",
            border_style="cyan",
            box=box.DOUBLE,
            expand=False,
        )
    )


def show_play_again_options():
    table = Table.grid(padding=(0, 2))
    table.add_column(style="bold white")
    table.add_column(style="white")
    table.add_row("1", "[green]Yes[/green]")
    table.add_row("2", "[red]No[/red]")
    console.print(Panel(table, title="PLAY AGAIN?", border_style="cyan", box=box.ROUNDED))


def show_message(message, style="white"):
    console.print(Panel(f"[{style}]{message}[/{style}]", border_style=style.split()[-1]))


def pause(message="\nPress Enter to continue..."):
    console.input(message)


def small_delay():
    sleep(0.25)
