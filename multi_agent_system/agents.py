import asyncio

class BaseAgent:
    async def run(self, input_data):
        raise NotImplementedError


class PlannerAgent(BaseAgent):
    async def run(self, task):
        await asyncio.sleep(1)
        print("🧠 Planner：拆解任务")

        return {
            "steps": [
                "写引言",
                "介绍AI自动化",
                "举例多Agent系统",
                "总结"
            ]
        }


class ExecutorAgent(BaseAgent):
    async def run(self, plan):
        await asyncio.sleep(1)
        print("⚙️ Executor：执行任务")

        content = ""
        for step in plan["steps"]:
            content += f"{step}内容...\n"

        return {"content": content}


class ReviewerAgent(BaseAgent):
    async def run(self, execution):
        await asyncio.sleep(1)
        print("🔍 Reviewer：审核内容")

        content = execution["content"]

        status = "通过" if len(content) > 20 else "不合格"

        return {
            "status": status,
            "final_content": content
        }
