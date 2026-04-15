import os
import datetime
import subprocess

class WorkFlowSkill:
    """WorkBuddy 工作流程 Skill 示例：日常任务处理 + 自动推送到 GitHub"""

    def __init__(self, repo_path: str, commit_msg_prefix: str = "Daily work update"):
        self.repo_path = repo_path
        self.commit_msg = f"{commit_msg_prefix} {datetime.date.today()}"

    def step1_fetch_task(self):
        """步骤1：拉取今日任务"""
        print("[步骤1] 拉取今日工作任务...")
        tasks = [
            "需求分析",
            "代码开发",
            "单元测试",
            "文档编写"
        ]
        print(f"今日任务：{tasks}")
        return tasks

    def step2_execute_work(self):
        """步骤2：执行工作"""
        print("[步骤2] 正在执行工作流程...")
        print("工作执行完成")

    def step3_generate_report(self):
        """步骤3：生成工作日报"""
        print("[步骤3] 生成今日工作报告")
        report = f"""
# 工作日志 {datetime.date.today()}
1. 完成需求梳理
2. 完成核心模块开发
3. 完成自测
4. 提交版本
"""
        # 保存到文件
        report_file = os.path.join(self.repo_path, "daily_report.md")
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"报告已保存：{report_file}")

    def step4_push_to_github(self):
        """步骤4：自动推送代码/文件到 GitHub"""
        print("[步骤4] 开始推送至 GitHub 仓库...")

        commands = [
            'git add .',
            f'git commit -m "{self.commit_msg}"',
            'git push origin main'
        ]

        os.chdir(self.repo_path)

        for cmd in commands:
            try:
                result = subprocess.run(
                    cmd, shell=True,
                    capture_output=True,
                    text=True,
                    encoding="utf-8"
                )
                if result.stdout:
                    print(result.stdout)
                if result.stderr and "error" in result.stderr.lower():
                    print("推送异常：", result.stderr)
            except Exception as e:
                print(f"执行失败 {cmd}: {e}")

        print("GitHub 推送完成\n")

    def run(self):
        """运行完整 Skill 工作流"""
        print("===== WorkBuddy 工作流 Skill 启动 =====")
        self.step1_fetch_task()
        self.step2_execute_work()
        self.step3_generate_report()
        self.step4_push_to_github()
        print("===== 全部流程执行完毕 =====")


if __name__ == "__main__":
    # ========== 请修改为你的 GitHub 仓库本地路径 ==========
    GIT_REPO_LOCAL_PATH = "C:\Users\24378\Desktop\omgomgomg"

    skill = WorkFlowSkill(repo_path=GIT_REPO_LOCAL_PATH)
    skill.run()