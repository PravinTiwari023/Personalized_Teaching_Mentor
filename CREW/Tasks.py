from textwrap import dedent
from crewai import Task

class ProjectTasks():
    def Planning(self, agent, project_scope, project_objective, available_resources, technology_stack):
        return Task(
            description=dedent(f"""\
            Develop a strategic plan focusing on the execution of the project within the constraints of the available resources. This plan should leverage the skill sets encapsulated within the available resources to achieve the project objectives, aligning closely with the specified technology stack.

            Project Scope: {project_scope}
            Project Objective: {project_objective}
            Available Resources: {available_resources}
            Technology Stack: {technology_stack}"""),

            expected_output=dedent("""\
            A strategic execution plan that details the roles and contributions of the available resources towards meeting the project's objectives. The plan should delineate the division of labor, ensuring the technology stack is aptly utilized throughout the development process. Additionally, it should outline strategies for maximizing each resource's potential to navigate project challenges effectively."""),
            agent=agent,
            async_execution=True)
    def Research(self, agent, project_scope, project_objective, available_resources, technology_stack):
        return Task(
            description=dedent(f"""\
            Conduct thorough research to understand how the project's scope and objectives can be achieved with the current team composition and technology stack. This involves analyzing the capabilities of the available resources - a front-end developer, a back-end developer, a data scientist, and a software tester - and determining how these can be optimized to meet the project goals. Additionally, explore the technology stack to identify any gaps or advantages it presents in relation to the project's needs.

            Project Scope: {project_scope}
            Project Objective: {project_objective}
            Available Resources: {available_resources}
            Technology Stack: {technology_stack}"""),

            expected_output=dedent("""\
            A comprehensive research report that outlines:
            - How each member of the team can contribute to achieving the project objectives, considering their specific roles and expertise.
            - Any potential challenges or limitations posed by the available resources and how these can be mitigated.
            - The compatibility of the technology stack with the project's needs and any adjustments or enhancements needed.
            The report should provide actionable insights and recommendations for leveraging the team's capabilities and the technology stack to successfully execute the project."""),
            agent=agent,
            async_execution=True)

    def Coding(self, agent, project_scope, project_objective, available_resources, technology_stack):
        return Task(
            description=dedent(f"""\
            Execute the development phase of the project according to the strategic plan, focusing on coding practices that adhere to the project scope and objectives. Utilize the available resources efficiently, ensuring that each team member leverages their expertise within the defined technology stack to create robust, scalable, and maintainable code.

            Project Scope: {project_scope}
            Project Objective: {project_objective}
            Available Resources: {available_resources}
            Technology Stack: {technology_stack}

            Emphasize the importance of collaborative coding, peer reviews, and the integration of best coding practices to enhance the quality and performance of the software. Identify key functionalities and modules that require development and assign them to the appropriate resources, taking into consideration their skills and the project's timeline."""),

            expected_output=dedent("""\
            A set of well-documented, tested, and high-quality codebases that align with the project's objectives and scope. This includes completed code modules for each identified functionality, adherence to the project's technology stack, and successful integration of all components. The output should reflect a collaborative effort among the available resources, showcasing efficiency in task distribution and utilization of the team's collective expertise."""),
            agent=agent)

    def Testing(self, agent, project_scope, technology_stack, available_resources):
        return Task(
            description=dedent(f"""\
            Initiate the testing phase, ensuring comprehensive coverage across all developed features within the project scope. This phase should utilize the technology stack and available resources to conduct a variety of tests, including unit, integration, system, and acceptance testing. The goal is to identify and rectify any bugs or issues that could impact the functionality, performance, or user experience of the final product.

            Project Scope: {project_scope}
            Technology Stack: {technology_stack}
            Available Resources: {available_resources}

            Focus on creating detailed test cases and automated test scripts that align with the project objectives. Prioritize collaboration and communication among team members to facilitate efficient bug tracking and resolution. Leverage the expertise of the available resources to ensure a thorough examination of both the codebase and user experience."""),

            expected_output=dedent("""\
            A comprehensive test report detailing the outcomes of all conducted tests, highlighting identified bugs, issues, and areas for improvement. The report should also include documentation of test cases, automated test scripts, and any relevant data collected during the testing process. Ultimately, the testing phase should ensure that the software meets all defined requirements and quality standards before it moves to deployment."""),
            agent=agent)
