# 0x00. MySQL Advanced

## Description

This project focuses on advanced MySQL concepts, including **database optimization, stored procedures, triggers, views, and functions**. You will practice creating tables with constraints, optimize query performance using indexes, and explore how to automate tasks with triggers and stored procedures.

Throughout the project, you’ll be expected to:
- Create well-structured databases with constraints.
- Leverage MySQL indexing to optimize query performance.
- Implement reusable stored procedures and functions.
- Automate tasks using triggers.
- Simplify data retrieval using views.

The goal is to help you understand how these advanced features can improve database performance and maintainability.

---

## Learning Objectives

By the end of this project, you should be able to:
- **Create tables** with appropriate constraints (e.g., `PRIMARY KEY`, `UNIQUE`, `FOREIGN KEY`).
- **Optimize queries** by adding indexes to columns.
- **Implement stored procedures and functions** for reusable SQL logic.
- **Create views** to simplify data queries.
- **Implement triggers** to automate tasks based on database events (INSERT, UPDATE, DELETE).

---

## Project Requirements

- **Environment:** Ubuntu 18.04 LTS using **MySQL 5.7 (version 5.7.30)**.
- **Comments:** All SQL files must contain a comment explaining the task just above the query.
- **Formatting:** SQL keywords should be written in **uppercase** (e.g., `SELECT`, `WHERE`).
- **Files:** Ensure all SQL files end with a new line and are properly named for each task.
- **README:** A `README.md` file at the root of the project is required.
- **Execution:** Files will be tested using the `wc` command to check length.

---

## Getting Started

To complete this project, use the **"container-on-demand"** platform with Ubuntu 18.04. You can connect via SSH or WebTerminal. Follow the steps below to start MySQL:

```bash
$ service mysql start
# Output: MySQL Community Server 5.7.30 is started
