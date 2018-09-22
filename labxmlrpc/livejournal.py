from lj import lj


ljclient = lj.LJServer("Python-Blog3/1.0", "http://daniil-r.ru/bots.html; i@daniil-r.ru")
ljclient.login("soa_test", "Labs2018")
ljclient.postevent("Awesome post", "Awesome subject", props={"taglist": "github, livejournal"})