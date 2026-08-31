# Shared Understanding · 认知外显

**不是让 AI 一直问你，而是让它主动把自己的理解和假设讲清楚。**

An output-first Agent Skill for making the agent's working understanding visible.

版本：`0.1.0` · 纯指令技能 · 无运行依赖 · 中文正文，可按用户语言响应

## 它解决什么问题

你让 agent 做一个网页登录。它做了账号验证和登录页面，却没有保持刷新后的登录状态，最后告诉你「登录完成」。

问题不只是代码遗漏：它把“登录”理解成了什么、作了什么简化，你始终不知道。你也不应该靠逐行读代码才能发现。

这个 skill 要求它主动说：

> 当前实现只在页面不刷新的情况下保持登录；刷新后会退出。我暂时把身份放在页面内存里，这是我自行采用的简化，不是你要求的。刷新保留登录还是未补齐的体验缺口，不能据此说完整登录已完成。

这样你可以及时补充「刷新当然也要保持」。更好的 agent 会在实现前主动考虑这种自然预期，在授权范围内补齐并验证，而不是等你发现。

**披露不是为缺陷免责。** 这个 skill 不允许用“你没说”合理化明显缺口，也不鼓励先选一个差方案再声明假设。

## 与提问型 skill 的区别

- 提问型流程：agent 提问 → 用户补充输入 → agent 形成理解。
- 本技能：agent 呈现已经形成的理解 → 用户不回复也能看懂 → 需要时可纠正 → agent 更新并继续。

普通工作不因一次认知呈现而暂停。必要的授权、安全或真实阻塞问题另行处理，本技能既不新增例行审批，也不绕过已有授权边界。

## 它会呈现什么

1. 它认为你要实现的结果，以及它采用的任务解释。
2. 用户明确要求和实际检查到的事实。
3. 它作出的推断、未经确认但已采用的假设。
4. 它已经选择的方案及简短依据。
5. 这些选择造成的实际行为、未覆盖的自然预期和限制。
6. 哪些已验证，哪些只是假定可行。

完整的是影响当前结果的工作理解，不是内部思维链。默认先给一段摘要，复杂内容再分层展开；小任务可能只需要一句。关键假设必须出现在对话里，不能仅藏在文档中。

开始时呈现当前理解；中途有变化时呈现差量；被纠正时撤回旧假设并调整行动；交付时说明实际能力与理解之间的差距。没有变化就不机械重复。

## 安装到 Codex

仓库目前用于私有试用，下面的 GitHub 克隆需要相应仓库权限。

```sh
gh repo clone Neighhhbor/shared-understanding-skill
cd shared-understanding-skill
```

在仓库根目录执行下面的命令，把技能链接到个人技能目录。它不会覆盖已有同名技能，修改仓库内的技能内容也会同步生效：

```sh
skill_source="$PWD/skills/shared-understanding"
skill_destination="$HOME/.agents/skills/shared-understanding"
if [ ! -f "$skill_source/SKILL.md" ]; then
  printf '%s\n' '请先进入 shared-understanding-skill 仓库根目录。'
elif [ -e "$skill_destination" ] || [ -L "$skill_destination" ]; then
  printf '%s\n' '同名技能已存在，未覆盖；请检查已有安装。'
else
  mkdir -p "$HOME/.agents/skills"
  ln -s "$skill_source" "$skill_destination"
fi
```

Codex 支持个人技能目录与符号链接。若列表没有更新，重启 Codex。不要同时安装多份同名技能；符号链接依赖本仓库位置，移动或删除仓库后需要重新连接。[官方技能文档](https://learn.chatgpt.com/docs/build-skills)

其他支持 Agent Skills 的宿主，可将 `skills/shared-understanding` 整个文件夹放进其官方技能目录；`agents/openai.yaml` 是可选 Codex 元数据。这里没有测试其他宿主，不承诺它们的自动触发方式相同。

## 使用

在 Codex 中显式调用：

```text
$shared-understanding 帮我实现网页的用户登录功能。
```

也可以针对已有工作请求一份当前认知快照：

```text
$shared-understanding 先把你目前对这项工作的理解、事实依据、假设、
已经采用的选择和未覆盖的体验呈现出来，不要用一轮提问代替说明。
```

技能描述允许隐式匹配，但**隐式触发不是保证，安装也不等于每轮都会执行**。先在新任务中显式调用，观察实际输出。某些宿主不会将上一轮技能调用自动延续到后续轮次。

若希望项目中持续应用，可自行把以下短约定合并到已有 `AGENTS.md`；不要覆盖原文件：

```md
## 认知外显

对实质性工作，使用已安装的 shared-understanding skill，主动呈现当前任务解释、
事实依据、推断与假设、已采用的选择、未覆盖的自然预期和验证边界。
当理解变化时及时呈现差量；不要用例行追问或审批替代解释。
简单明确的任务直接处理；现有安全和授权边界不变。
```

这类宿主指令有助于持续应用，但仍不是确定性的执行拦截器。[Codex 项目指令机制](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

## 文件导航

- [技能正文](skills/shared-understanding/SKILL.md)：实际生效的指令，也是最值得自己修改的文件。
- [正反例](skills/shared-understanding/references/examples.md)：登录刷新、搜索范围、取消任务、用户纠正等。
- [行为评测场景](evals/cases.json)：12 个场景，包含多轮情况。
- [评测方式与状态](evals/README.md)：区分文件检查、模型行为和真实用户理解。
- [包检查](tests/test_package.py)：Python 标准库测试，无需安装依赖。

```sh
python3 -m unittest discover -s tests -v
```

## 验证边界

包检查只检查格式、文件引用、元数据和评测用例结构，不证明模型会稳定遵守，也不证明用户一定理解。行为评测场景当前标为 `not_run`，尚未完成真实模型的基线/技能对照或用户试用评测。

本技能的目标是增加理解的可见性和可纠正性，而不是保证“消除所有假设”。不能读心，不能强制所有宿主自动加载，也不能代替产品判断、正确实现与实际测试。

不收集遥测，不保存聊天记录，不包含外部调用、安装钩子或后台服务。测试产生的本地评测记录默认被 Git 忽略；不要把私人项目上下文提交到共享仓库。

## 修改你的版本

优先调整三件事：你希望看到的表达颗粒度、常被遗漏的自然预期示例、什么变化值得立即更新。不要把它逐渐改回“每步问我是否同意”。新增规则时，同时增加一个能暴露旧版本问题的评测场景。

格式参考：[Agent Skills 规范](https://agentskills.io/specification)、[OpenAI 技能编写文档](https://learn.chatgpt.com/docs/build-skills)。技能正文与示例针对认知外显目的编写，不要求安装其他技能框架。
