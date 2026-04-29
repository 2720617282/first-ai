class Orchestrator:
    def __init__(self):
        self.agents = {}

    def register_agent(self, name, agent):
        self.agents[name] = agent

    async def run(self, task):
        print(f"开始任务: {task['goal']}")

        plan = await self.agents["planner"].run(task)
        execution = await self.agents["executor"].run(plan)
        review = await self.agents["reviewer"].run(execution)

        return review
