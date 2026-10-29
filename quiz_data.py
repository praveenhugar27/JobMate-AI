"""Question banks for SQL and role-specific learning missions."""

QUIZ_LEVELS = [
    {
        "name": "SQL Basics",
        "unlock_after": None,
        "description": "SELECT, WHERE, ORDER BY, COUNT(), and DISTINCT",
        "questions": [
            {
                "question": "1. Which SQL command retrieves data from a table?",
                "options": ["INSERT", "SELECT", "UPDATE", "DELETE"],
                "answer": "SELECT",
                "explanation": "SELECT retrieves data from a table.",
            },
            {
                "question": "2. Which clause filters rows in a query?",
                "options": ["ORDER BY", "GROUP BY", "WHERE", "SELECT"],
                "answer": "WHERE",
                "explanation": "WHERE filters rows using a condition.",
            },
            {
                "question": "3. Which clause sorts query results?",
                "options": ["SORT", "ORDER BY", "ARRANGE", "FILTER"],
                "answer": "ORDER BY",
                "explanation": "ORDER BY sorts results in ascending or descending order.",
            },
            {
                "question": "4. Which function counts rows?",
                "options": ["SUM()", "TOTAL()", "COUNT()", "NUMBER()"],
                "answer": "COUNT()",
                "explanation": "COUNT() counts rows or non-NULL values, depending on its argument.",
            },
            {
                "question": "5. Which keyword removes duplicate rows from a result?",
                "options": ["UNIQUE", "DISTINCT", "SINGLE", "DIFFERENT"],
                "answer": "DISTINCT",
                "explanation": "DISTINCT removes duplicate rows from the result.",
            },
        ],
    },
    {
        "name": "SQL Aggregation",
        "unlock_after": "SQL Basics",
        "description": "GROUP BY, HAVING, SUM(), AVG(), and aggregate queries",
        "questions": [
            {
                "question": "1. Which function calculates the total of numeric values?",
                "options": ["COUNT()", "SUM()", "AVG()", "ROUND()"],
                "answer": "SUM()",
                "explanation": "SUM() adds numeric values in a column or expression.",
            },
            {
                "question": "2. Which function calculates the arithmetic mean?",
                "options": ["MEAN()", "MID()", "AVG()", "TOTAL()"],
                "answer": "AVG()",
                "explanation": "AVG() calculates the average of non-NULL numeric values.",
            },
            {
                "question": "3. Which clause groups rows with the same values?",
                "options": ["ORDER BY", "GROUP BY", "WHERE", "DISTINCT"],
                "answer": "GROUP BY",
                "explanation": "GROUP BY combines rows into groups based on selected columns.",
            },
            {
                "question": "4. Which clause filters grouped results after aggregation?",
                "options": ["WHERE", "ORDER BY", "HAVING", "FROM"],
                "answer": "HAVING",
                "explanation": "HAVING filters groups, often using aggregate conditions.",
            },
            {
                "question": "5. A table has sales amounts 10, 20, and 30. What does SUM(amount) return?",
                "options": ["20", "30", "60", "3"],
                "answer": "60",
                "explanation": "SUM(amount) adds 10 + 20 + 30, which equals 60.",
            },
        ],
    },
    {
        "name": "SQL Joins & Subqueries",
        "unlock_after": "SQL Aggregation",
        "description": "INNER JOIN, LEFT JOIN, and subqueries",
        "questions": [
            {
                "question": "1. Which join returns only rows with matching values in both tables?",
                "options": ["INNER JOIN", "LEFT JOIN", "CROSS JOIN", "FULL OUTER JOIN"],
                "answer": "INNER JOIN",
                "explanation": "INNER JOIN returns rows where the join condition matches in both tables.",
            },
            {
                "question": "2. Which join keeps every row from the left table, even without a match?",
                "options": ["INNER JOIN", "LEFT JOIN", "CROSS JOIN", "SELF JOIN"],
                "answer": "LEFT JOIN",
                "explanation": "LEFT JOIN keeps all left-table rows and fills unmatched right-table columns with NULL.",
            },
            {
                "question": "3. A subquery is best described as:",
                "options": [
                    "A query nested inside another query",
                    "A table permanently deleted by SQL",
                    "A command that sorts all rows",
                    "A database connection setting",
                ],
                "answer": "A query nested inside another query",
                "explanation": "A subquery is a query used inside another SQL statement.",
            },
            {
                "question": "4. Which clause usually specifies how two tables are matched in a join?",
                "options": ["GROUP BY", "ON", "HAVING", "LIMIT"],
                "answer": "ON",
                "explanation": "The ON clause states the join condition between tables.",
            },
            {
                "question": "5. Table Employees has department_id values and table Departments has id values. Which condition matches them?",
                "options": [
                    "Employees.department_id = Departments.id",
                    "Employees.name = Departments.id",
                    "Employees.department_id > Departments.id",
                    "Employees.id = Departments.department_name",
                ],
                "answer": "Employees.department_id = Departments.id",
                "explanation": "Matching the employee's department_id to the department table's id connects each employee to the relevant department.",
            },
        ],
    },
]

ROLE_QUIZZES = {
    "Data Analyst": [
        {
            "name": "Data Analyst — Python Basics",
            "description": "Python fundamentals for analysing data",
            "questions": [
                {
                    "question": "1. Which Python library is commonly used to work with tabular data?",
                    "options": ["Flask", "Pandas", "Turtle", "Tkinter"],
                    "answer": "Pandas",
                    "explanation": "Pandas provides DataFrame structures for working with tabular data.",
                },
                {
                    "question": "2. Which Pandas function reads a CSV file?",
                    "options": ["pd.open()", "pd.read_csv()", "pd.load_table()", "pd.import_csv()"],
                    "answer": "pd.read_csv()",
                    "explanation": "pd.read_csv() loads CSV data into a DataFrame.",
                },
                {
                    "question": "3. Which measure represents the arithmetic average?",
                    "options": ["Median", "Mode", "Mean", "Range"],
                    "answer": "Mean",
                    "explanation": "The mean is calculated by dividing the sum by the number of values.",
                },
                {
                    "question": "4. Which chart is generally useful for comparing values across categories?",
                    "options": ["Bar chart", "Scatter plot only", "Network graph", "Map only"],
                    "answer": "Bar chart",
                    "explanation": "Bar charts make comparisons between categories easy to see.",
                },
                {
                    "question": "5. What is the main purpose of data cleaning?",
                    "options": [
                        "To introduce more rows",
                        "To fix or handle data quality problems",
                        "To change every value to text",
                        "To remove all columns",
                    ],
                    "answer": "To fix or handle data quality problems",
                    "explanation": "Data cleaning addresses missing, duplicate, inconsistent, or invalid data.",
                },
            ],
        },
    ],
    "Software Engineer": [
        {
            "name": "Software Engineer — Python Fundamentals",
            "description": "Variables, functions, and programming logic",
            "questions": [
                {
                    "question": "1. Which Python type represents a whole number?",
                    "options": ["str", "int", "list", "dict"],
                    "answer": "int",
                    "explanation": "The int type represents integers such as 4 and -2.",
                },
                {
                    "question": "2. Which keyword defines a function in Python?",
                    "options": ["func", "define", "def", "function"],
                    "answer": "def",
                    "explanation": "Python functions are defined using the def keyword.",
                },
                {
                    "question": "3. Which data structure stores an ordered, mutable sequence?",
                    "options": ["tuple", "list", "set", "None"],
                    "answer": "list",
                    "explanation": "Lists preserve order and allow their contents to be changed.",
                },
                {
                    "question": "4. What does a for loop commonly do?",
                    "options": [
                        "Repeats code over an iterable",
                        "Defines a class",
                        "Imports a package",
                        "Stops the Python interpreter permanently",
                    ],
                    "answer": "Repeats code over an iterable",
                    "explanation": "A for loop iterates through items in an iterable.",
                },
                {
                    "question": "5. Which structure is used to handle an exception?",
                    "options": ["if/else only", "try/except", "for/in", "def/return"],
                    "answer": "try/except",
                    "explanation": "try/except lets a program handle specified exceptions.",
                },
            ],
        },
    ],
    "Data Scientist": [
        {
            "name": "Data Scientist — Statistics & ML",
            "description": "Statistics and introductory machine learning",
            "questions": [
                {
                    "question": "1. What does a labelled training dataset contain?",
                    "options": [
                        "Features and known target values",
                        "Only file names",
                        "Only missing values",
                        "No observations",
                    ],
                    "answer": "Features and known target values",
                    "explanation": "Supervised learning uses features paired with known target labels or values.",
                },
                {
                    "question": "2. What does overfitting mean?",
                    "options": [
                        "A model performs well on training data but generalises poorly",
                        "A dataset contains no columns",
                        "A model never learns from data",
                        "Every prediction is identical",
                    ],
                    "answer": "A model performs well on training data but generalises poorly",
                    "explanation": "An overfit model captures training-specific patterns that do not generalise well.",
                },
                {
                    "question": "3. Which measure is less affected by extreme values?",
                    "options": ["Mean", "Median", "Maximum", "Range"],
                    "answer": "Median",
                    "explanation": "The median depends on the middle rank and is generally more robust to outliers than the mean.",
                },
                {
                    "question": "4. Why use a test dataset?",
                    "options": [
                        "To estimate performance on unseen data",
                        "To guarantee perfect accuracy",
                        "To duplicate training labels",
                        "To remove every feature",
                    ],
                    "answer": "To estimate performance on unseen data",
                    "explanation": "A held-out test set helps estimate how well a model generalises.",
                },
                {
                    "question": "5. In supervised learning, what is a feature?",
                    "options": [
                        "An input variable used by a model",
                        "Always the final prediction",
                        "The model's source-code filename",
                        "A database password",
                    ],
                    "answer": "An input variable used by a model",
                    "explanation": "Features are input variables used to make predictions.",
                },
            ],
        },
    ],
    "Web Developer": [
        {
            "name": "Web Developer — Web Fundamentals",
            "description": "HTML, CSS, JavaScript, and browser basics",
            "questions": [
                {
                    "question": "1. What is HTML mainly used for?",
                    "options": [
                        "Structuring webpage content",
                        "Managing database backups",
                        "Training machine-learning models",
                        "Configuring computer memory",
                    ],
                    "answer": "Structuring webpage content",
                    "explanation": "HTML defines the structure and meaning of webpage content.",
                },
                {
                    "question": "2. What is CSS mainly used for?",
                    "options": [
                        "Styling webpage elements",
                        "Querying SQL tables",
                        "Writing operating-system drivers",
                        "Creating database indexes",
                    ],
                    "answer": "Styling webpage elements",
                    "explanation": "CSS controls presentation, layout, and visual styling.",
                },
                {
                    "question": "3. Which language commonly adds interactivity in the browser?",
                    "options": ["SQL", "JavaScript", "CSS", "Markdown"],
                    "answer": "JavaScript",
                    "explanation": "JavaScript can respond to user actions and update webpage behaviour.",
                },
                {
                    "question": "4. Which HTML element creates a hyperlink?",
                    "options": ["<p>", "<a>", "<table>", "<img>"],
                    "answer": "<a>",
                    "explanation": "The anchor element creates hyperlinks, typically using the href attribute.",
                },
                {
                    "question": "5. What does HTTP primarily define?",
                    "options": [
                        "Communication rules for web requests and responses",
                        "A Python list structure",
                        "A CSS colour palette",
                        "A SQL aggregation function",
                    ],
                    "answer": "Communication rules for web requests and responses",
                    "explanation": "HTTP is a protocol used for communication between web clients and servers.",
                },
            ],
        },
    ],
}
