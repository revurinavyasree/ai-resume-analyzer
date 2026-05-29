SKILL_QUESTIONS = {
    "python": [
        "What are Python's key features compared to Java?",
        "Explain list, tuple, set and dict with examples.",
        "What is OOP? Explain with a Python example.",
        "What are decorators in Python?",
        "Difference between deep copy and shallow copy.",
    ],
    "java": [
        "What is the difference between JDK, JRE, and JVM?",
        "Explain the four pillars of OOP in Java.",
        "What is the difference between ArrayList and LinkedList?",
        "What are checked and unchecked exceptions?",
        "Explain the concept of multithreading in Java.",
    ],
    "sql": [
        "What is the difference between INNER JOIN and LEFT JOIN?",
        "Explain normalization and its types (1NF, 2NF, 3NF).",
        "Difference between DELETE, TRUNCATE, and DROP.",
        "What is an index and why is it used?",
        "Write a query to find the second highest salary.",
    ],
    "dsa": [
        "What is the time complexity of binary search?",
        "Explain the difference between stack and queue.",
        "What is a linked list? When would you use it over an array?",
        "Explain BFS and DFS with a real-world use case.",
        "What is dynamic programming? Give an example.",
    ],
    "oops": [
        "Explain the four pillars of OOP with examples.",
        "What is the difference between abstraction and encapsulation?",
        "What is method overloading vs method overriding?",
        "What is an interface? How is it different from an abstract class?",
        "Explain the SOLID principles.",
    ],
    "dbms": [
        "What is the difference between DBMS and RDBMS?",
        "Explain ACID properties with examples.",
        "What is a foreign key and why is it important?",
        "Difference between clustered and non-clustered index.",
        "What is a transaction? How is it managed?",
    ],
    "os": [
        "What is a process vs a thread?",
        "Explain deadlock and how to prevent it.",
        "What is virtual memory?",
        "Explain paging and segmentation.",
        "What is a semaphore?",
    ],
    "networking": [
        "What is the OSI model? Explain each layer.",
        "Difference between TCP and UDP.",
        "What is DNS and how does it work?",
        "Explain HTTP vs HTTPS.",
        "What is an IP address? Difference between IPv4 and IPv6.",
    ],
    "git": [
        "What is the difference between git merge and git rebase?",
        "Explain git clone, pull, push, and fetch.",
        "What is a branch in git? Why do we use it?",
        "How do you resolve a merge conflict?",
        "What is .gitignore?",
    ],
    "aws": [
        "What are the core services of AWS?",
        "Explain EC2, S3, and RDS in simple terms.",
        "What is IAM in AWS?",
        "Difference between vertical and horizontal scaling.",
        "What is a load balancer?",
    ],
    "machine learning": [
        "What is the difference between supervised and unsupervised learning?",
        "Explain overfitting and how to prevent it.",
        "What is the difference between classification and regression?",
        "What is a confusion matrix?",
        "Explain the bias-variance tradeoff.",
    ],
    "html": [
        "What is semantic HTML? Give examples.",
        "Difference between div and span.",
        "What are HTML5 new features?",
        "What is the purpose of the DOCTYPE declaration?",
        "Explain the difference between block and inline elements.",
    ],
    "css": [
        "What is the box model in CSS?",
        "Difference between flexbox and grid.",
        "What is CSS specificity?",
        "How does responsive design work in CSS?",
        "What are CSS variables?",
    ],
    "javascript": [
        "What is the difference between var, let, and const?",
        "Explain promises and async/await.",
        "What is the DOM and how do you manipulate it?",
        "What is event bubbling and capturing?",
        "Difference between == and ===.",
    ],
    "react": [
        "What is the virtual DOM?",
        "Explain useState and useEffect hooks.",
        "What is the difference between props and state?",
        "What is React component lifecycle?",
        "What are controlled and uncontrolled components?",
    ],
}

COMPANY_QUESTIONS = {
    "TCS": [
        "Why do you want to join TCS?",
        "What is TCS's flagship product or platform? (TCS BaNCS, Ignio)",
        "Tell me about yourself in 2 minutes.",
        "Where do you see yourself in 3 years at TCS?",
        "What do you know about TCS NQT?",
    ],
    "Infosys": [
        "Why Infosys over other IT companies?",
        "What is Infosys Lex platform?",
        "Describe a project you built and the tech stack used.",
        "How do you handle pressure and tight deadlines?",
        "What is the InfyTQ certification and have you completed it?",
    ],
    "Wipro": [
        "Why do you want to work at Wipro?",
        "What do you know about Wipro WILP program?",
        "Describe your final year project.",
        "How would you rate your communication skills and why?",
        "What is your understanding of IT service delivery?",
    ],
    "Accenture": [
        "Why Accenture?",
        "What do you know about Accenture's Technology or Operations division?",
        "Tell us about a time you solved a complex problem.",
        "Are you comfortable relocating for work?",
        "What is your experience with Agile methodology?",
    ],
    "Cognizant": [
        "Why do you want to join Cognizant?",
        "What is a GenC or GenC Next role at Cognizant?",
        "Describe a team project you contributed to.",
        "How do you stay updated with new technologies?",
        "What is your preferred tech stack and why?",
    ],
    "Capgemini": [
        "Why Capgemini?",
        "What do you know about Capgemini's RISE with SAP offering?",
        "Describe a challenge you faced in a project and how you overcame it.",
        "Are you open to working in client-facing roles?",
        "How do you prioritize tasks when given multiple assignments?",
    ],
    "IBM": [
        "Why IBM?",
        "What do you know about IBM Cloud or Watson?",
        "Describe your experience with any open-source tools.",
        "How comfortable are you with Linux/command line?",
        "What does DevOps mean to you?",
    ],
    "Deloitte": [
        "Why Deloitte Technology?",
        "What is your understanding of IT consulting?",
        "Describe a time you used data to solve a problem.",
        "How do you communicate technical concepts to non-technical people?",
        "What is your experience with Excel or BI tools?",
    ],
    "EY (Ernst & Young)": [
        "Why EY Technology?",
        "What is digital transformation and why does it matter?",
        "Describe a situation where you showed leadership.",
        "How do you handle feedback and criticism?",
        "What tools have you used for data analysis?",
    ],
}


def generate_questions(skills, company=None):
    output = {}

    # Skill-based questions
    for skill in skills:
        if skill in SKILL_QUESTIONS:
            output[skill] = SKILL_QUESTIONS[skill]

    # Company-specific questions
    if company and company in COMPANY_QUESTIONS:
        output[f"{company} — HR & Company Questions"] = COMPANY_QUESTIONS[company]
    elif not company:
        # Return all company questions if no specific company selected
        for comp, qs in COMPANY_QUESTIONS.items():
            output[f"{comp} — HR Questions"] = qs[:2]  # 2 per company to avoid overload

    return output