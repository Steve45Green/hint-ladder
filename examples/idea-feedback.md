# Idea feedback: a graded web project (Projeto Integrado)

Prompt: *"Idea feedback, please: for Projeto Integrado (graded) I want to build a PHP + SQL Server web app where students book lab rooms, with login, admin approval and email notifications, in 6 weeks, alone."*

---

**Idea feedback**

**Verdict:** adjust — solid idea that hits the right course concepts (auth, authorization, MVC, PDO/DB design, integration with an external service), but the scope as stated is tight for 6 weeks solo once you account for SQL Server setup friction and the concurrency logic a booking system actually needs.

**Strengths**
- Login + admin approval gives you two distinct roles to demonstrate authentication *and* authorization (STYLE/course-relevant: session handling, `password_hash`, access checks) — exactly what Web Application Development grades.
- The domain (rooms, time slots, bookings) is small enough to model cleanly in a handful of tables, which is good for the "integrated project" unit's structure/deployment goals.
- Email notification is a nice, bounded way to show integration with an external service without ballooning scope, *if* you keep it to one or two trigger points (booking approved/rejected).

**Risks**
- **SQL Server from PHP is the biggest hidden cost.** `sqlsrv`/`pdo_sqlsrv` driver install (and ODBC on Linux, or a SQL Server container) tends to eat the first days of a solo project if you haven't already got it running. This is worth derisking in week 1, not week 3.
- **Booking overlap is a real concurrency problem, not just a form.** "Prevent double-booking the same room/slot" needs either a transaction with a row lock or a unique/exclusion constraint check at insert time — easy to hand-wave in the plan and then discover a race condition during testing.
- **Approval workflow adds a state machine** (pending/approved/rejected) layered on top of ownership checks (a student must not see or cancel another student's booking — classic IDOR territory) — more surface area than it looks like on paper.
- **Email sending from a dev environment** often gets silently blocked; if you don't plan a logging fallback, you can lose days debugging "it just doesn't send."
- Six weeks solo covering DB design + auth + CRUD + approval + email + deployment + write-up is workable only if you cut secondary features early (e.g., no recurring bookings, no room categories/search filters, no calendar-widget polish) rather than trying to trim late.

**Questions**
1. Is the stack framework-free PHP or is a framework (e.g., Laravel) allowed/expected? This alone can double or halve your timeline for routing/auth/MVC scaffolding.
2. Does the rubric specify required features explicitly (e.g., a REST API, tests, specific security controls), or is scope entirely your call — and have you actually gotten a PHP→SQL Server connection working yet?
3. What does "admin approval" need to support — just approve/reject, or also edit/override a booking? That changes the state machine's size.

**Alternatives to know about:** Laravel (routing/auth/ORM scaffolding), PHPMailer/Symfony Mailer for the email piece, FullCalendar.js for a booking calendar UI if you have time later.

Your `MISSION.md` still has the assessment weights/dates and success criteria marked "to confirm" — worth locking those down (via `/course`) before you commit to this scope, since the rubric will tell you which of the above risks actually matter for your grade.
