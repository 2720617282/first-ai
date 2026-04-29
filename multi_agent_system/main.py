import asyncio
from agents import PlannerAgent, ExecutorAgent, ReviewerAgent
from orchestrator import Orchestrator

async def main():
    orchestrator = Orchestrator()

    orchestrator.register_agent("planner", PlannerAgent())
    orchestrator.register_agent("executor", ExecutorAgent())
    orchestrator.register_agent("reviewer", ReviewerAgent())

    task = {
        "id": 1,
        "goal": "写一篇关于AI自动化的博客",
        "status": "pending"
    }

    result = await orchestrator.run(task)

    print("\n最终结果：")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
