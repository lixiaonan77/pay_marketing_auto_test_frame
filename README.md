# pay_marketing_auto_test_frame
🎯 项目介绍
基于Python+pytest+Allure+RabbitMQ+GitHub Action 搭建【纯正七层分层】企业级测试开发框架
主打业务：营销活动 + 第三方支付核心链路 + MQ异步消息状态同步

✅ 覆盖完整真实业务场景
1.用户每日签到、自动发放用户积分流程校验
2.iPhone限量大奖抽奖活动（库存仅1个、30天仅限中奖1次、中奖有效期30天、高并发规则校验）
3.创建订单 + 唤起第三方支付宝支付 + 异步回调结果重试轮询
4.支付成功后通过RabbitMQ MQ异步同步订单状态、用户权益生效、业务状态流转

✅ 框架核心亮点
1.标准七层分层架构：配置层/公共层/工具层/数据层/接口层/用例层/报告层
2.完全实现配置分离、数据分离、代码低耦合高复用
3.YAML统一管理环境、账号、业务测试数据，拒绝硬编码
4.全局Session会话保持+Token全局夹具，全程只登录一次共享令牌
5.tenacity异步重试装饰器，专门适配支付、MQ消费延迟场景
6.原生完整Excel工具类：自动去空格、空值处理、自动转列表字典、传统数据驱动兼容
7.RabbitMQ+pika封装：MQ连接、生产者发消息、消费者监听消费、业务状态校验
8.Allure高颜值可视化测试报告
9.GitHub Action 定时CI/CD自动执行回归测试

✅ 技术栈
Python / pytest / requests / pika / yaml / tenacity / Allure-report / GitHub Action