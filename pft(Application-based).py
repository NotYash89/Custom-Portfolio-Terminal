import tkinter as tk

PROMPT = "ysx:~$ "

app = tk.Tk()
app.title("YSX Terminal")
app.geometry("1000x700")
app.configure(bg="black")

terminal = tk.Text(app,bg="black",fg="white",insertbackground="white",font=("JetBrains Mono", 15),relief="flat",wrap="word")
terminal.pack(fill="both", expand=True,padx=15,pady=15)
terminal.insert("end","Welcome to Yashank's Terminal\n""Copyright (c) 2026 Yashank. All rights reserved.\nType 'help' to get started.\n\n")
terminal.insert("end", PROMPT)

commands = {
    "help": "Available commands:\nhelp\nabout\nversion\nsocials\nclear\nMore commands soon!",
    "about": "This is a custom terminal portfolio made by Yashank.",
    "version": "alpha-v1.0.1",
    "socials": """Instagram : https://www.instagram.com/dyinglight.09/
Github    : https://github.com/NotYash89
LinkedIn  : www.linkedin.com/in/yashank-sogra-6b9811410
Reddit    : https://www.reddit.com/user/Responsible_Gold3854/
X         : https://x.com/Notyash97""",
    
"projects": """
    1.
        Name             : Custom Portfolio Terminal
        Description      : An interactive terminal-style portfolio
                           application that lets visitors explore my
                           work using CLI commands instead of
                           traditional webpage navigation. Includes
                           input sanitization and state protection.
        Status           : Published
        Version          : alpha-v0.1
        Category         : Desktop Application / Portfolio
        Tech-stack       : Python 3.12, Tkinter
        Highlights       : Custom CLI, Interactive Commands,
                           Input Validation, State Protection
        Github Repo Link : https://github.com/NotYash89/Custom-Portfolio-Terminal

    2.
        Name             : Quit Doom Scrolling
        Description      : A Godot-based game project built around
                           the concept of breaking away from
                           endless scrolling through an
                           interactive gaming experience.
        Status           : Published / Development
        Version          : Beta Testing
        Category         : Game Development
        Tech-stack       : Godot Engine, GDScript
        Highlights       : Game Scenes, 3D Terrain,
                           Interactive Gameplay
        Github Repo Link : https://github.com/NotYash89/Quit-Doom-Scrolling

    3.
        Name             : Team Phoenix Official
        Description      : The official website of Team Phoenix,
                           created to showcase the team's identity,
                           members, achievements, and projects.
                           Includes an administrative dashboard
                           for managing project information.
        Status           : Public Repository
        Version          : V5.0
        Category         : Web Development / Team Platform
        Tech-stack       : HTML5, CSS3, JavaScript,
                           Firebase Authentication, Firestore
        Highlights       : Multi-page Website, Admin Dashboard,
                           Team Profiles, Project Management,
                           Achievement Showcase
        Github Repo Link : https://github.com/NotYash89/Team-Phoenix-Official

    4.
        Name             : AirIndex - Synthetic Prototype
        Description      : A prototype airfare analytics platform
                           designed to measure flight ticket price
                           movements across India. Demonstrates
                           price index calculations, comparable
                           fare analysis, and visualization of
                           airfare trends using synthetic data.
        Status           : Prototype
        Version          : Not specified
        Category         : Data Analytics / Statistical Platform
        Tech-stack       : HTML5, CSS3, JavaScript, JSON
        Highlights       : Airfare Index, Jevons Methodology,
                           Synthetic Dataset, Interactive
                           Dashboard, Price Trend Analysis
        Github Repo Link : https://github.com/NotYash89/AirIndex-Synthetic-Prototype

    5.
        Name             : Vighnaharta
        Description      : N/A
        Status           : Public Repository
        Version          : Not specified
        Category         : Not specified
        Tech-stack       : Not specified
        Highlights       : Repository documentation available
        Github Repo Link : 

     6.
        Name             : ForgeMatch
        Description      : A data-driven candidate ranking and
                           matching system developed for the
                           INDIA.RUNS Data & AI Challenge.
                           Designed to evaluate candidate
                           profiles against job requirements,
                           calculate suitability scores, and
                           generate ranked recommendations.
        Status           : Hackathon Submission Completed
        Version          : Final Submission
        Category         : Data Science / AI / Ranking Systems
        Tech-stack       : Python, Data Processing,
                           Scoring and Ranking Algorithms
        Highlights       : Candidate Evaluation,
                           Multi-Factor Ranking,
                           Automated Scoring,
                           Data Analysis,
                           Ranked Candidate Output
        Event            : INDIA.RUNS Data & AI Challenge 2026
        Team             : ForgeMatch
        Github Repo Link : https://github.com/nikitasingh1617/ForgeMatch

    UNDER DEVELOPMENT/ UPCOMING PROJECTS

    7.
        Name             : EDGECASE
        Description      : An upcoming software project
                           currently in active development.
                           Focused on building an innovative
                           and practical solution.
        Status           : Under Development
        Version          : N/A
        Category         : Software Development
        Tech-stack       : To Be Announced
        Github Repo Link : Private / Not Available

    ----------------------------------------------------------------------------------
    Total Original Repositories : 7
    GitHub Profile              : https://github.com/NotYash89
    ----------------------------------------------------------------------------------
""",

}


def get_current_command():
    line = terminal.get("insert linestart", "insert lineend")
    return line.replace(PROMPT, "").strip()


def execute_command(event=None):
    command = get_current_command().lower()

    terminal.insert("end", "\n")

    if command == "clear":
        terminal.delete("5.0", "end")

    elif command in commands:
        terminal.insert("end", commands[command] + "\n")

    elif command:
        terminal.insert("end", f"Unknown command: {command}\n")

    terminal.insert("end", "\n" + PROMPT)
    terminal.see("end")

    return "break"



def protect_prompt(event):
    current_line = terminal.get("insert linestart", "insert lineend")

    if not current_line.startswith(PROMPT):
        terminal.mark_set("insert", "end-1c")

    return None


terminal.bind("<Return>", execute_command)
terminal.bind("<Key>", protect_prompt)

terminal.focus()

app.mainloop()
