text = '''Considering OSIV/OEMIV is widely considered an anti-pattern, OpenEntityManagerInViewInterceptor should IMO not be enabled by default. Rather than that it should be opt-in.
If this proposal isn't accepted at the very least the default behavior should be stressed properly in the documentation. Currently the only reference is in configuration properties appendix.


I agree. I think we should change the default in 2.0.
 Would anyone care to elaborate? I definitely see it's a controversial topic, but I think that 'widely considered anti-pattern' is quite a bit of a stretch. It had been an anti-pattern in the days (< Spring 2.0) when O(S|E)IV automatically meant opening a transaction, too, but whenever I see someone (esp. from the CDI camp) arguing O(S|E)IV is a bad idea, the next step that usually follows is exposing a request scoped EntityManager which is exactly the same thing with the same advantages and problems.

So I'd love to learn what's wrong with the default setting? Judging from the projects I see, I guess everyone would then just turn it on manually.

IMO if you have a transactional unit-of-work whose result of execution requires further fetching from database that occurs after the aforementioned unit-of-work has ended I don't know how adding behavior that supports such data access pattern can be described not being an anti-pattern. Same for not having well defined transactional boundaries. Anyway not to go any further here my thoughts on this topic have been covered in @vladmihalcea's blog post better than I could express them myself. I respect that everyone has their preferences when it comes to data access but I cannot agree this is not an anti-pattern.


Well, my experience is just the opposite. 😄

What's wrong with the current default settings is that adds behavior that's too opinionated to address the complex subject of lazy loading of associations. Even worse, it does so completely silently, because as described in my original comment, its only mention is in the configuration properties appendix. I'd also argue this is bad for novice developers as it completely hides lazy loading concerns from them, rather then have them face such concerns and decide how to address them after educating on the topic.

If someone wants OSIV, they'll enable it with a single configuration property first time they face the LazyInitializationException.


I can't really follow the sentence here. That's circular reasoning, isn't it? Because you describe it as anti-pattern you can't see how it cannot be described as such. Hm.
I just re-read Vlad's blog and still remain unconvinced. Actually, I agree with everything he writes there. Still, there's nothing that inherently breaks code when an O(S|E)IVF is in place. Yes, its usage can cause suboptimal query performance and all other kinds of suboptimal effects if you don't know what you're doing. The thing is: if you start to argue that way, you basically have to shun JPA entirely. Yes, it's quite easy to suboptimally configure mappings, query executions etc. Still, I'd fix those problems when they actually occur to become some.
Quite the opposite picture without an O(S|E)IVF: fundamental things you naively (read: not being a JPA/Hibernate expert like Vlad, you, me (?)) expect to work — like traversing a property (e.g. while rendering a view) — will just stop working. Now you can of course go ahead and raise the experts finger, tell people to read Vlad's blog and then do the "right thing"™. I'd argue most people will rather do one of two things: activate O(S|E)IVF again and just live with the slight decrease in performance, or — even worse — rather extend their transaction boundaries as this might seem as the even more easy thing to do. I mean, why would you use an OR mapper if not for convenience. If you want to optimize the heck out of your relational data access, you're probably down to SQL anyway.
I personally have never seen any real problems being caused by the EntityManager (and thus the connection) being held open during view rendering. If that really becomes a performance problem: there's an easy way to turn that off. Not being able to traverse a model in the view and being forced into DTOing every entity is a much more cumbersome default. Note that one of Boot's core goals is to provide a great developer experience. Following the "but it might not be the most optimal way of working", we would never have started with things like Spring Data (JPA), as you can clearly create non-optimal queries OOTB if you're not deeply into the store characteristics.
I don't think O(S|E)IV is too opinionated, as it's not the thing that imposes the opinion. JPA does in the first place. O(S|E)IV just causes fundamental things to continue to work as non-JPA experts expect them to work. I am not even saying O(S|E)IV is an optimal solution but the current setup is trading a working and potentially suboptimal OOTB experience over an experience that requires very deep understanding and looks like it's not working OOTB.
So I end up wondering what real benefit hanging the default has I am not aware of any real problems stemming from the current default that have been brought up here and we'd basically just cater a different opinion, with the very likely chance that if the default was changed, the other camp would just again ask for it to be reverted again. 

To use or not to use OSIV is an architectural decision, and, in the good spirit of DevOps, the DBA must be involved when making all these decisions because OSIV can become a performance issue only in a production environment, not on a developer machine.

From a developer perspective, OSIV is very attractive since it can boost productivity. However, if you're not involved in tuning the enterprise system and scaling it with the ever increasing incoming throughput, you'll have a very optimistic view on OSIV or temporary Session anti-pattern.

Both Spring and Hibernate offer some opinionated options, but, in the end, it is the responsibility of the DevOps team to decide whether a given feature makes sense for their particular system.

Therefore, this option should be explicitly activated.
@olivergierke I'm sorry but your take on this with statements like if you start to argue that way, you basically have to shun JPA entirely sounds like it's all or nothing with JPA. IMO where it (JPA/Hibernate) excels the most are the write scenarios, persisting complex graphs with added value in features like locking mechanisms. OTOH with reads you have so many options to choose from, and I (as well as many others) prefer to be explicit with what I fetch and how exactly I fetch it from the database. Such things should IMO not be dictated by your mappings.

Also I have a problem with statement that If that really becomes a performance problem: there's an easy way to turn that off - you won't get yourself out of that kind of a problem by simply turning off OSIV. If you had relied on OSIV while developing your app and you have to turn it off at some point down the road, that will almost certainly require a fair share of refactoring of your data access related code.


What I was trying to get across that JPA is already a trade-off. A quite huge one, especially favoring developer convenience over performance / efficiency (as otherwise you'd use more low-level technology like SQL in the first place). So blaming O(S|E)IV for producing suboptimal results in some cases is quite a stretch.

In case you find any of the effects O(S|E)IV are really becoming a problem in your application, you can switch of the defaults, still use a manually configured O(S|E)IV bound to the paths that just work fine with it and tweak the problematic scenarios. Heck, depending on what problem you really run into, you can still use Vlad's great advice to optimize mappings and queries even with the O(S|E)IV present.

I'd always rather act on problems when they appear rather than hastily DTOing my entire codebase in anticipatory obedience. Isn't the latter a great example of premature optimization? Also, always remember that with the current setup there's nothing preventing you from doing all the things you'd like. We solely argue OOTB developer experience, a default, and I'd argue that this should be less invasive to the overall code design than what it'd be if what's suggested is applied.

I read the whole thread and I can only agree that OSIV is an anti-pattern.

My point here is not about performance but about architectural design. I mean it's called Open Session in View for a reason, right? Not only do we handle database-related stuff in the view layer - which is wrong from a conceptual point of view, what happens if an exception happens while the response stream is being written? The page has only partially being served to the client so the stack trace gets written here as well... There's no way to handle nicely it.

That's the original sin of OSIV: it breaks in a very bad way one of the basics of software development - separation of concerns.

(Bragging rights: I might even have been one of the first to describe OSIV as an anti-pattern as such back in 2010 when it was all "it's described in the Hibernate book so you're plain wrong").

My 2 cents.
How is that an O(S|E)IV specific problem? Exceptions can be caused by anything.That feels quite constructed to me. Following that train of thought, you can argue that an @Transactional is violating this concern as well as you mix a technical thing with your business logic. It feels like you're trying to decouple for the reason of decoupling, and by that actually create incentives for users to create much more technical code than probably necessary. At some point you have to connect things to things, don't you?

So again, what hazardous problems are caused by O(S|E)IV being the default, that are introduced by O(S|E)IV actually, and not some upstream technology decision? I can probably stop repeating that I totally see the potential downsides of using it 🙃. I just think the benefits of letting it be the default — again, nobody's forcing anyone to actually use it — introduces totally outweigh the drawbacks that could occur under certain conditions. '''