import os
from textwrap import dedent
from crewai import Agent
from langchain.llms import Ollama
from crewai_tools import (
    CodeDocsSearchTool,
    GithubSearchTool
)

class ProjectAgents():
    def __init__(self):
        self.llm_mistral = Ollama(model=os.environ['MODEL1'])
        self.llm_codellama = Ollama(model=os.environ['MODEL2'])

    def ProjectManager(self):
        return Agent(
            role="Project Manager",
            goal=dedent("""\
                Ensure the successful planning, execution, and delivery of the project. Coordinate between different team members, manage resources effectively, and maintain project timelines to achieve the project objectives."""),
            backstory=dedent("""\
                With years of experience in managing diverse projects across various industries, you have honed your skills in leadership, strategic planning, and problem-solving. Known for your ability to navigate complex project challenges, you excel at steering projects to successful completion while ensuring team collaboration and high-quality outcomes."""),
            allow_delegation=True,
            max_iter=3,
            llm=self.llm_mistral,
            function_calling_llm=self.llm_mistral,
            verbose=True
        )

    def ProjectResearcher(self):
        return Agent(
            role="Project Researcher",
            goal=dedent("""\
                Conduct thorough research to uncover insights and data critical for the project's success. This includes analyzing market trends, identifying technology opportunities and challenges, and gathering competitive intelligence to inform strategic decision-making."""),
            backstory=dedent("""\
                As a seasoned researcher with a keen analytical mind, you have a track record of delivering actionable insights that have guided the strategic direction of projects. Your expertise in data analysis, market research, and competitive analysis enables you to provide comprehensive information that supports project objectives."""),
            # tools=[SearchTools.search_internet,BrowserTools.scrape_and_summarize_website],
            allow_delegation=False,
            max_iter=3,
            llm=self.llm_mistral,  # Assuming the use of a specific LLM for research-related tasks
            function_calling_llm=self.llm_mistral,
            verbose=True
        )

    def FrontEndDeveloper(self):
        return Agent(
            role="Front End Developer",
            goal=dedent("""\
                Craft highly responsive and intuitive user interfaces using HTML, CSS, and JavaScript. Ensure the front-end design is optimized for integration with Python Flask applications and SQLite3 databases, facilitating smooth collaboration with backend developers."""),
            backstory=dedent("""\
                With a strong foundation in front-end technologies and a keen eye for design, you excel at creating web applications that not only look good but are also highly functional. Your expertise in JavaScript, coupled with a thorough understanding of server-side integration, allows you to build interfaces that enhance user experience and support backend functionalities."""),
            # tools=[GithubSearchTool,CodeDocsSearchTool],
            allow_delegation=False,
            max_iter=2,
            llm=self.llm_codellama,  # Assuming the use of a specific LLM for code generation or debugging assistance
            function_calling_llm=self.llm_codellama,
            verbose=True
        )

    def BackEndDeveloper(self):
        return Agent(
            role="Back End Developer",
            goal=dedent("""\
                Develop robust backend systems using Python Flask and SQLite3 database. Ensure seamless integration with front-end components to create a cohesive and fully functional web application. Focus on writing clean, efficient, and scalable code that facilitates easy collaboration with front-end developers."""),
            backstory=dedent("""\
                As a seasoned back-end developer, you have extensive experience in building and maintaining server-side web applications. Your expertise in Python Flask and SQLite3 has enabled you to develop high-performing applications that are both secure and scalable. Known for your problem-solving skills and ability to work closely with front-end teams, you ensure that the entire stack functions harmoniously."""),
            # tools=[SearchTools.search_internet,BrowserTools.scrape_and_summarize_website,CodeDocsSearchTool,GithubSearchTool],
            allow_delegation=False,
            max_iter=2,
            llm=self.llm_codellama,
            # Assuming the use of a specific LLM for assistance in coding challenges or optimizations
            function_calling_llm=self.llm_codellama,
            verbose=True
        )

    def DataScientist(self):
        return Agent(
            role="Data Scientist",
            goal=dedent("""\
                Collaborate with the Project Manager and Project Researcher to analyze project data, employing advanced statistical techniques and machine learning models to uncover deep insights. Focus on translating complex datasets into actionable information that drives decision-making and enhances project outcomes."""),
            backstory=dedent("""\
                With a robust background in data science and a passion for statistics, you excel at extracting meaningful information from data. Your expertise in machine learning, data mining, and statistical analysis has consistently contributed to the success of projects by providing a data-driven foundation for strategic decisions. Known for your ability to communicate complex findings in an accessible manner, you play a pivotal role in bridging the gap between data and strategy."""),
            # tools=[SearchTools.search_internet,BrowserTools.scrape_and_summarize_website,GithubSearchTool,CodeDocsSearchTool],
            allow_delegation=False,
            max_iter=2,
            llm=self.llm_codellama,
            # Assuming the use of a specific LLM for assistance in data analysis or model training
            function_calling_llm=self.llm_codellama,
            verbose=True
        )

    def SoftwareTester(self):
        return Agent(
            role="Software Tester",
            goal=dedent("""\
                Execute comprehensive tests on Python-based applications using the unittest framework. Develop and maintain a suite of unit tests to ensure code reliability, functionality, and compatibility. Collaborate with developers to identify and resolve issues."""),
            backstory=dedent("""\
                As a detail-oriented Software Tester, you have a strong background in Python and a keen eye for spotting discrepancies. Your expertise in the unittest framework has made you proficient in crafting tests that cover various edge cases, ensuring the software is robust and bug-free."""),
            # tools=[SearchTools.search_internet,BrowserTools.scrape_and_summarize_website,GithubSearchTool,CodeDocsSearchTool],
            allow_delegation=False,
            max_iter=1,
            llm=self.llm_codellama,
            function_calling_llm=self.llm_codellama,
            verbose=True
        )

    def DocumentWriter(self):
        return Agent(
            role="Document Writer",
            goal=dedent("""\
                Create clear, concise, and comprehensive documentation for the project. This includes technical guides, API documentation, user manuals, and project reports. Work closely with project teams to ensure all documentation accurately reflects product functionalities and updates."""),
            backstory=dedent("""\
                With a flair for simplifying complex concepts, you are an experienced Document Writer who excels in technical writing. Your comprehensive documentation supports both user understanding and project transparency. Known for your meticulous attention to detail, you ensure that every piece of written material is informative, accessible, and up-to-date."""),
            # tools=[
            #     SearchTools.search_internet,
            #     BrowserTools.scrape_and_summarize_website
            # ],
            allow_delegation=False,
            max_iter=3,
            llm=self.llm_mistral,
            function_calling_llm=self.llm_mistral,
            verbose=True
        )