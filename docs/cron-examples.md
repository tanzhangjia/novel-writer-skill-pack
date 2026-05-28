# Cron 任务配置

## 续写（每天6:00）
```json
{"name":"novel-write","schedule":{"kind":"cron","expr":"0 6 * * *","tz":"Asia/Shanghai"}}
```

## 脑暴（早8/中14/晚20）
```json
{"name":"brainstorm-morning","schedule":{"kind":"cron","expr":"0 8 * * *","tz":"Asia/Shanghai"}}
{"name":"brainstorm-afternoon","schedule":{"kind":"cron","expr":"0 14 * * *","tz":"Asia/Shanghai"}}
{"name":"brainstorm-evening","schedule":{"kind":"cron","expr":"0 20 * * *","tz":"Asia/Shanghai"}}
```

## 反思（每天16:00）
```json
{"name":"reflection","schedule":{"kind":"cron","expr":"0 16 * * *","tz":"Asia/Shanghai"}}
```
