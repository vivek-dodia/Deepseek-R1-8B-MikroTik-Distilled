# Thread Information
Title: Thread-1115748
Section: RouterOS
Thread ID: 1115748

# Discussion

## Initial Question
Hi, I’m having an issue with sending emails from my router based on logging rules. I believe the SMTP configuration is correct because when I try to send an email manually using Tool > Email > Send Email, the email is delivered without any problems.I’m attaching screenshots of the logging configuration. I intentionally triggered an IPSec error, which appeared in the logs, but no email was sent.I also tried setting up email logging to use echo. When sending manually, the echo appeared, but it seems that the router didn’t even attempt to send an email when the error occurred.Thank you for your help! ---

## Response 1
Have you set anyemail-toaddress in the/system/logging/actionconfiguration? There is no default recipient in the/tool/e-mailsettings.Can you re-word the "I also tried setting up email logging to use echo" part? I did not understand what you actually did - for me, thetargetof an action can be eitherechooremail, not both. So did you use two rows of/system/loggingwith sametopicsanddifferentaction, and then when you generated a log event matching both these rows, the echo appeared but no attempt to send an e-mail happened? ---

## Response 2
Hello, I can confirm - have the same issue.When I set to send email on INFO topic, the mail is being sent, but when I set topics like error or system, the e-mail is not sent and there is no contact to e-mail server.HW: CCR1009 (on tile) and v.7.16 ---