from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from .tools.serper_tool import serper_tool

@CrewBase
class SocialActivityOfAPerson():
    """SocialActivityOfAPerson crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_agent'], 
            tools=[serper_tool],
            verbose=True
        )

    @agent
    def professional_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['professional_analyst'], 
            tools=[serper_tool],
            verbose=True
        )

    @agent
    def reputation_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['reputation_checker'], 
            tools=[serper_tool],
            verbose=True
        )

    @agent
    def profile_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['profile_analyzer'], 
            verbose=True
        )

    @agent
    def narrative_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['narrative_writer'], 
            verbose=True
        )


    @agent
    def cultural_fit_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['cultural_fit_evaluator'], 
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            output_file='research_task.md'
        )

    @task
    def professional_background_task(self) -> Task:
        return Task(
            config=self.tasks_config['professional_background_task'],
            output_file="professional_background.md"
            )

    @task
    def reputation_check_task(self) -> Task:
        return Task(
            config=self.tasks_config['reputation_check_task'],
            output_file="reputation_check.md"
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'],
            context=[
                self.research_task(),
                self.professional_background_task(),
                self.reputation_check_task()],
            output_file='analysis_task.md'
        )

    @task
    def culture_fit_task(self) -> Task:
        return Task(config=self.tasks_config['culture_fit_task'],
            context=[
                self.research_task(),
                self.professional_background_task(),
                self.reputation_check_task(),
                self.analysis_task()],
            output_file='cultural_fit.md'
        )


    @task
    def story_task(self) -> Task:
        return Task(
            config=self.tasks_config['story_task'],
            context=[
                self.research_task(),
                self.professional_background_task(),
                self.reputation_check_task(),
                self.analysis_task(),
                self.culture_fit_task()],
            output_file='life_story.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SocialActivityOfAPerson crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True
        )
