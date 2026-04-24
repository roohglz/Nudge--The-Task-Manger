A task manager built while learning to build.

What is this?
Nudge is a full-stack task manager I built as a hands-on way to deeply understand Object-Oriented Programming in Python — not just read about it, but actually implement every concept in a real, working project.
I'm a CS (AI) student currently on my placement preparation journey. I know a lot of this theory already — but I came back to rebuild it from scratch because I believe understanding something and being able to build something with it are two very different things.
This project is both a portfolio piece and a personal milestone.

What it does

Add Personal, Work, and Urgent tasks
Set priorities — Low, Medium, High
Update status on personal tasks — pending, in progress, done
Delete tasks
Flash messages for success and error feedback
Clean, sleek dark UI built with Flask + vanilla HTML/CSS


What I built it with
LayerTechBackendPython, FlaskOOPsCustom class hierarchyFrontendHTML, CSS, Jinja2 templatesConceptsAbstraction, Encapsulation, Inheritance, Polymorphism

OOPs concepts implemented
This wasn't just a Flask project — every class was designed intentionally to demonstrate a concept:
ConceptWhere it livesAbstractionBaseTask — abstract base class with execute() and get_details()EncapsulationPersonalTask.__status — private attribute with @property getter/setter + validationInheritancePersonalTask, WorkTask inherit from BaseTask via super()Multiple InheritanceUrgentWorkTask(WorkTask, UrgentMixin)Polymorphismexecute() behaves differently across all task typesMROVisible in UrgentWorkTask.__mro__Class methodTaskManager.get_total_tasks()Static methodTaskManager.validate_priority()CompositionTaskManager holds a list of task objectsDunder methods__str__, __repr__, __eq__, __len__Method chainingmanager.add_task(t1).add_task(t2).add_task(t3)Duck typingTasks used polymorphically without type checking@property decoratorPythonic getter/setter on PersonalTask.status

Project structure
nudge-task-manager/
├── tasks.py          # all OOPs classes
├── app.py            # Flask backend
├── main.py           # testing file
├── templates/
│   └── index.html    # frontend
├── static/
│   └── style.css     # styling
└── README.md

How to run it
bash# Clone the repo
git clone https://github.com/yourusername/nudge-task-manager

# Install dependencies
pip install flask

# Run the app
python app.py
Open http://127.0.0.1:5000 in your browser.

Built with curiosity. Rebuilt with intention.