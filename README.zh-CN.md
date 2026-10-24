<div align="center">

# OpenFirst Engineering

**项目审计、开源复用、根因诊断、UI/UX 收敛、项目救援与发布决策**

[![Tests](https://github.com/vincentlovesnake-maker/openfirst-engineering/actions/workflows/tests.yml/badge.svg)](https://github.com/vincentlovesnake-maker/openfirst-engineering/actions/workflows/tests.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB.svg)](https://www.python.org/)

[English](README.md) | [简体中文](README.zh-CN.md)

</div>

OpenFirst Engineering（OFE）是面向 Codex 和 AI 编程 Agent 的工程决策与交付控制
Skill，覆盖项目审计、开源项目改造、Build vs. Reuse、根因诊断、工程规划、受控
实施、UI/UX 质量门禁、项目救援和发布就绪。

它帮助 Agent 决定：**应该开发什么、保留什么、复用什么、集成什么、修复什么、
停止什么，以及什么条件下可以交付或发布**。

它要求先核实当前项目，再比较原生能力和成熟开源方案，明确权限、证据、风险、
回滚和停止条件，最终选择满足验收要求的最小改动。它不会把“写了很多代码、生成
了很多文档、发现了很多问题”当成成功。

## 什么时候使用 OFE

- 一个项目反复修改、候选越来越多，却始终无法正式交付；
- 需要独立项目审计，区分当前事实、历史报告、Mock、Fixture、演示和口头声明；
- 一个 Bug、生产故障或 UI 问题反复出现，需要复现、竞争假设和根因诊断；
- 需要比较保留、配置、复用、集成、Fork、替换和最小自研；
- 需要把开源 Web 项目、AI Agent 或自动化系统改造成 Windows、桌面端、移动端或行业产品；
- UI 看起来廉价、混乱、不一致、难操作或无障碍不足，但不希望无边界重做全站；
- AI、Agent、RAG、数据、安全、许可证、部署或商业承诺需要有证据的工程裁决；
- 发布前需要版本身份、质量、回滚、许可证、支持和客户交付门禁；
- 需要冻结范围、去重阻断项、停止无效工作，并找到项目最短正确闭环。

适用检索词包括：**项目审计、开源选型、开源改造、软件架构决策、根因分析、
UI/UX 审计、项目救援、发布就绪、Windows 客户端封装、AI Agent 工程化**。

## 核心能力

| 能力 | OFE 的作用 |
|---|---|
| 当前项目核查 | 区分当前源码和运行证据、历史报告、演示、Fixture 与 Mock |
| 开源优先 | 按原生能力、已有依赖、隐藏路径、配置适配、成熟开源、最小自研的顺序决策 |
| 模式路由 | 根据真实目标和权限选择主模式，而不是机械匹配关键词 |
| 权限边界 | 规划和审计默认只读，只有明确授权才能实施 |
| 证据分级 | 区分事实、推断、未知、建议和争议结论 |
| 质量门禁 | 为正确性、安全、可靠性、交付、许可证和商业条件定义可观察标准 |
| UI/UX 质量门禁 | 要求真实渲染旅程、状态与视口覆盖、可访问性、失败恢复，以及功能/视觉/交互/可访问性独立结论 |
| 最小改动 | 优先保留稳定行为、已有数据和上游兼容性 |
| 项目收口 | 明确负责人、依赖、验收、回滚、复测和停止条件 |
| 专业角色 | 提供 81 个责任合同，但不会冒充真实独立评审人员 |
| 结构化工具 | 提供只读清点、Finding 校验和决策报告校验脚本 |

## 八种工作模式

| 模式 | 适用决策 | 典型产出 |
|---|---|---|
| `MODE-01 PROJECT_INCEPTION` | 是否应该建设产品或新能力 | 建设、集成、延期或拒绝决策 |
| `MODE-02 OPEN_SOURCE_TRANSFORMATION` | 如何改造已有开源系统 | 保留上游兼容的改造路线 |
| `MODE-03 ENGINEERING_PLANNING` | 如何把批准目标转化为可执行任务 | 架构、边界、任务、门禁和回滚 |
| `MODE-04 CONTROLLED_IMPLEMENTATION` | 如何实施已批准的有限范围 | 有边界的变更和当前版本验证 |
| `MODE-05 PROJECT_AUDIT` | 项目当前真实状态如何 | 有证据的发现、风险和限制 |
| `MODE-06 ROOT_CAUSE_DIAGNOSIS` | 一个具体故障为何持续发生 | 复现、因果链、最小控制和复测条件 |
| `MODE-07 PROJECT_RESCUE_AND_CLOSURE` | 如何停止反复返工并完成收口 | 冻结的退出条件和收口计划 |
| `MODE-08 RELEASE_READINESS` | 候选版本能否交付或发布 | GO、条件通过、不通过或延期依据 |

## UI/UX 质量门禁

UI/UX 是横向伴随门禁，不是第九种生命周期模式。用户界面审计仍使用 MODE-05，
持续界面故障使用 MODE-06，获批的前端修改使用 MODE-04，发布裁决使用 MODE-08。

门禁会冻结界面版本、用户、核心旅程、状态、视口、设备或 DPI、输入方式、本地化、
现有设计系统和必须保护的业务行为；随后要求真实渲染证据，并分别记录功能、视觉、
交互和可访问性结果。

它禁止仅凭源码、HTTP 200、静态检测或单张截图批准 UI，也禁止在未诊断根因前更换
框架、通过隐藏功能制造整洁页面、不断叠加全局覆盖，或在代表性试点通过前推广全站。

## 开源优先顺序

```text
可见原生能力
  -> 隐藏、禁用或未接通能力
  -> 已安装依赖或框架能力
  -> 配置、适配器或插件
  -> 成熟外部开源方案
  -> 有边界的本地改进
  -> 最小必要自研
```

候选方案需要比较功能、维护、发布、Issue/PR、许可证、漏洞和供应链、平台与区域
适配、集成、迁移、测试、运维、回滚及总拥有成本。Star 数和漂亮 README 不能
单独作为采用依据。

决策词包括：`KEEP`、`REUSE_NATIVE`、`INTEGRATE`、`IMPROVE`、`REPLACE`、
`MINIMAL_BUILD`、`DEFER` 和 `REJECT`。

## 证据等级

| 等级 | 含义 |
|---|---|
| `E0` | 没有支撑的陈述 |
| `E1` | README、截图、文件名或声明等弱信号 |
| `E2` | 可追溯的当前源码、配置或 Schema 静态证据 |
| `E3` | 可重复的本地测试、构建或分析结果 |
| `E4` | 隔离环境端到端、迁移、恢复、性能或安全验证 |
| `E5` | 经授权且有来源链的生产、客户或商业结果 |

统一状态词包括：`CONFIRMED`、`RISK`、`UNVERIFIED`、`PASSED`、
`NOT_IMPLEMENTED`、`OUT_OF_SCOPE`、`RESOLVED` 和 `DISPUTED`。

`UNVERIFIED` 既不是通过，也不是缺陷；`PASSED` 必须具备当前基线、真实执行或
等价直接证据以及可核对结果。

## 权限等级

| 权限 | 边界 |
|---|---|
| `READ_ONLY` | 只检查和报告，不修改源码、配置或数据 |
| `PLAN_ONLY` | 只生成计划和模板，不实施业务变更 |
| `IMPLEMENT_SCOPED` | 只修改明确批准的范围 |
| `TEST_IN_SANDBOX` | 在隔离环境运行有成本边界的测试 |
| `RELEASE_PREPARATION` | 准备候选物和发布门禁，高影响动作仍需单独授权 |

生产写入、破坏性迁移、真实客户数据、凭据披露、许可证变更、公开商业信息和显著
付费调用需要明确授权。

## 安装

### Windows PowerShell

```powershell
git clone https://github.com/vincentlovesnake-maker/openfirst-engineering.git "$HOME\.codex\skills\openfirst-engineering"
```

### macOS 或 Linux

```bash
git clone https://github.com/vincentlovesnake-maker/openfirst-engineering.git \
  ~/.codex/skills/openfirst-engineering
```

安装后重启或刷新 Agent，并确认目录根部存在 `SKILL.md`。显式调用：

```text
$openfirst-engineering
```

## 使用示例

```text
使用 $openfirst-engineering。先调查当前项目已有功能与依赖，再执行开源优先 Gate，
比较 KEEP、REUSE_NATIVE、INTEGRATE 和 MINIMAL_BUILD，并区分已验证事实与未知项。
```

```text
使用 $openfirst-engineering 执行 MODE-05，权限为 READ_ONLY。不要把历史报告、
Mock 或演示数据作为当前通过证据，输出可追溯发现、限制和复测条件。
```

```text
使用 $openfirst-engineering 执行 MODE-02，评估把现有开源 Web Agent 包装为 Windows
客户端。保留上游行为，先比较成熟开源方案，再定义安装、启动、关闭、后台、升级、
回滚、卸载、数据位置、权限、离线、签名和平台支持验收。
```

```text
使用 $openfirst-engineering 执行 MODE-05，权限为 READ_ONLY，并激活
UI_UX_QUALITY_GATE。冻结界面基线，检查核心用户旅程及相关状态和视口，分别裁定
功能、视觉、交互和可访问性结果，定位规范化根因，并在全站推广前定义有边界的试点。
```

## 内置脚本

脚本仅使用 Python 标准库，不主动访问网络。

```bash
python scripts/inventory.py /path/to/project
python scripts/evidence_check.py findings.json --root /path/to/project
python scripts/validate_outputs.py report.json
```

## 输出合同

完整结果应包含模式、权限、基线、范围、事实、推断、未知、建议、原生能力清点、
开源 Gate、候选比较、明确决策、任务负责人、依赖、验收、回滚、完成定义、独立
复核或自我反审限制、实际验证以及完成状态。涉及用户界面时，还必须包含 UI/UX
门禁、真实渲染证据、试点边界，以及功能、视觉、交互和可访问性的独立结论。

完成状态为 `COMPLETE`、`PARTIAL`、`BLOCKED`、`DEFERRED` 或
`NO_CHANGE_NEEDED`。

## 仓库结构

```text
SKILL.md                         主规则与模式路由
agents/openai.yaml               Agent 展示信息和调用策略
references/                      模式、证据、安全、质量和角色规则
references/roles/                81 个专业责任合同
assets/                          比较、计划、UI/UX 审计、发布和收口模板
scripts/                         只读清点与结构化校验脚本
tests/                           单元、完整性、场景和行为测试
.github/workflows/tests.yml      Windows/Linux/macOS 持续集成
```

## 开发与验证

```bash
python -m unittest discover -s tests -v
python -m compileall -q scripts
```

CI 在 Windows、Linux 和 macOS 上使用 Python 3.10 与 3.13 验证，覆盖 Skill 发现
元数据、模式、权限、证据、开源决策、81 个角色、UI/UX 伴随门禁、结构化输出、
只读清点和场景基线。

## 明确限制

OFE 不是法律意见、安全认证或发布审批机构，也不会自动授予访问生产环境、客户
数据、密钥或付费 API 的权限。它不会因为新项目更流行就要求替换稳定系统，也
不会把实施者对自身重大修改的意见冒充独立评审。

## 参与贡献与许可证

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)、[SECURITY.md](SECURITY.md) 和
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。项目使用
[Apache License 2.0](LICENSE)，署名信息见 [NOTICE](NOTICE)。
