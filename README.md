# 务实旅行规划 · Realistic Travel Planner

先确认什么样的旅行适合你，再核实资料、安排路线。重点是作息、体力、
同行者、预算分配和体验取舍；按门到门时间安排交通，把排队、吃饭、休息
和行李计入行程，区分核心与可删项目，并解释哪些地方这次不值得去。

这是可移植的 Agent Skill，不是预订服务。它不会自动安装搜索、地图或票务
接口；动态事实仍需要宿主具备相应工具。回答使用旅行者的语言。

## 安装与使用

仓库内 `realistic-travel-planner/` 是可独立安装的 skill 文件夹；根目录的
测试、评估和 CI 用于维护与复查，不必放进技能目录。

Codex 用户把该文件夹放到自己的 `$CODEX_HOME/skills/`，未自定义时通常是
`~/.codex/skills/`。以 Windows PowerShell 为例，在仓库根目录执行：

```powershell
Copy-Item -LiteralPath .\realistic-travel-planner -Destination "$env:USERPROFILE\.codex\skills\realistic-travel-planner" -Recurse
```

目标文件夹若已存在，先比较本地改动，避免重复嵌套或覆盖自定义版本。
安装后在新会话中调用：

> 使用 $realistic-travel-planner，帮我规划旅行。先确认会改变路线的需求，
> 不要直接生成逐日攻略；信息不确定就明确说明。

其他支持 `SKILL.md` 的 agent 可按各自的技能目录规则安装。

## 工作方式

1. 复用已知信息，只问会改变决定的问题；关键信息未齐时先研究，不锁定逐日计划。
2. 为开放、预约、交通等关键事实保留来源、适用日期、查询时点和确定性状态。
3. 按体验优先级选核心项目，说明可删项目的增量时间、费用和删除条件。
4. 以门到门交通为基础，安排排队、正餐、恢复、取行李与机动余量。
5. 统一全队预算口径，检查已付费用、人数/间夜、应急金和可选项目费用。
6. 审查时间和费用；复杂时钟表与预算可运行内置 Python 检查器。

遇到缺票、体力不足、超时等情况，优先删减项目，保住核心体验和已确认的硬约束。

## 检查器与验证

Python 3.10+，只用标准库，不联网、不操作账户：

```shell
python -m unittest discover -s tests -v
python scripts/validate_package.py
python realistic-travel-planner/scripts/audit_plan.py evaluation/audit-example.json --constraints evaluation/audit-constraints.json
```

检查重叠、时长下限、开放/入场窗口、截止时间、费用数量、预算与应急金，
以及事先声明的必需项目/费用类别。独立约束文件用于避免通过修改草稿中的
预算和截止时间把错误“检查通过”。[JSON 契约](realistic-travel-planner/references/audit-schema.md)
适用于中间审计文件，不要求旅行者阅读或手工编写 JSON。

检查器只验证输入数据；不能证明路线/费用已完整列出、信息真实、预约有票、
体力合适或旅行体验优秀。跨时区、夏令时和跨午夜行程需按契约另外处理。

## 测试与其他 skill 的比较

见 [测试题](evaluation/cases.md)、[预先定义的观察标准](evaluation/rubric.md)、
[评估报告](evaluation/report.md) 和 [原始输出](evaluation/results/)。
同一组虚构证据用于三个独立 agent：本 skill、Adaptive Travel Planner、
Travel Planner Skill。上游版本固定到 Git 提交，原文没有复制进本仓库。

另有一次 [真实官网访问检查](evaluation/live-check.md)，如实记录了网页读取失败；
不把搜索摘要当成完成核验。小样本、单次运行、作者判读，不能据此宣称
比所有旅行 agent 更准确，也不能替代实际出游测试。

本项目的明确侧重是：简洁的需求确认、门到门排程、可删项目和跳过理由、
预算范围与数量核算，以及可复跑的确定性检查。天气/疲劳建模和 Wanderlog
集成等方面，现有项目各有优势，详见比较报告。

MIT 许可。示例全部为虚构测试数据；请勿把真实身份证件、支付资料、精确行踪
或个人健康信息提交到 public 仓库。
