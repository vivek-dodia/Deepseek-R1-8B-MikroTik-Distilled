# Thread Information
Title: Thread-214209
Section: RouterOS
Thread ID: 214209

# Discussion

## Initial Question
Hello, I have a question, we are talking about a small internet service provider that has about 800-1200 users and one or two cloud core routers.The question is, how to manage clients, IP addressing, and internet speed, with as little processor load as possible?There is such an idea that we use different subnets and VLANs, but limited resources, for exampleclient1 172.16.1.1/24 vlan101client2 172.16.2.1/24 vlan102...client1 172.16.254.1/24 vlan355Are there more rational ways? ---

## Response 1
You might want to take a look at PPPoE to manage to manage clients connection / IP addressing , etc..https://help.mikrotik.com/docs/spaces/R ... E-OverviewIt's easy to setup and deploy... ---

## Response 2
Will there be more offers?Are there any small or internet service providers in this forum?I've been asking this question for the entire time I've been on the forum and I'm not getting a correct answer ---

## Response 3
If you do not give the full story about your company & services, how could it be possible to even provide tips & tricks on this ?For sure PPPoE will be the most "cpu intensive" I think but it has advantages on scalability & operational level....and 800-1200 users is not much, so even using PPPoE could be done on a single box.How are you clients connected ? Cable ? Fiber ? Are you a WISP-type of provider ?Do you manage/own the last mile of cable to your clients ? Or do you "wholesale" from another local carrier or something?You provide sooooo little information so don't expect too much in return. ---

## Response 4
I don't really understand why it's important to know how services are provided, after all, the point is to manage the client from the central router.So, we provide services both via wisp and via gpon. Currently, clients have their own ip subnet and their own vlan. But I want to ask if there is some more optimal solution, how others behave. We provide clients with 50-100mbs of speed via wisp, and 100-500mbs of speed via gpon. ---

## Response 5
If you ask for free advices how to improve your payable services then IMHO you should unhide at least a little details and do not treat helpers as enemies. Otherwise you should consider hiring professional advisor that you could be snippy to. ---

## Response 6
Will there be more offers?Are there any small or internet service providers in this forum?I've been asking this question forthe entire time I've been on the forumand I'm not getting a correct answerAlso a comedian, the name associated with your accounts says "new user" and thus one could surmize you have not been around that long!As for the topic asked many times, I see only two other topics..... blocking a non-paying customer and some dell crap.......Did you look for any training or information on the subject like most professionals do......https://mynetworktraining.com/p/startin ... h-mikrotikhttps://www.udemy.com/course/starting-a ... -mikrotik/https://mum.mikrotik.com/presentations/ ... 022881.pdfhttps://mum.mikrotik.com/presentations/ ... 356910.pdfhttps://www.youtube.com/watch?v=lR31jTtbDKkHow hard do you really actually look.........methinks lazy as shit.Highly suggest -->https://mikrotik.com/consultants ---

## Response 7
Well, I'm not really a hater, I'm asking a serious simple question that I haven't received an answer from either me or any of the previous users. Also, I see you recommend consultants, so I've really called more than one and none of them helped. But as I mentioned, I solved this problem myselfOh, when you need help, maybe I can help. Because I only see one user currently offering a pppoe solution, I only hear more about configuration requests ---