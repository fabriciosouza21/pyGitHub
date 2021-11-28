issues = [ {
      "author":"Andy Wilkinson",
      "body":"See https://github.com/spring-projects/spring-boot/issues/10306#issuecomment-341761010",
      "id":10907,
      "updated_at":"03 November, 2017"
    },
    {
      "author":"Rob Winch",
      "body":"The behavior is quite intentional and I don't think it should change for the following reasons:\r\n\r\n- Prompting for HTTP Basic in a browser is less secure because\r\n  - There is no way to log out short of closing all the browser windows (and really who does this)\r\n  - HTTP Basic has no time out like a session\r\n  - HTTP Basic transfers a long term credential on every request increasing the likely hood of a long term credential leaking\r\n- Using HTTP Basic takes 1/2 second longer per request. When passwords are properly stored (i.e. using BCrypt) validation of the password should take 1/2 a second. This means that if HTTP Basic is being used, the response time is increased by 1/2 second per request (the credentials are validated on every request)\r\n- Requesting the endpoints with an accept type that does not include HTML will ensure that HTTP Basic is prompted. In a browser, users can append `.json` to the request URL to force HTTP Basic.\r\n- Preemptive HTTP Basic is supported for any accept type. This means that automated tooling will still work.\r\n- This is only the default behavior. The default security configuration is never going to be adequate for a real application, so we do expect users to modify this.\r\n- If the client has an accept type that allows for HTML, then a redirect to an HTML page should be expected as it is a much better user experience.",
      "id":10907,
      "updated_at":"03 November, 2017"
    },
    {
      "author":"Phil Webb",
      "body":"I'm very much against moving away from the Spring Security defaults and I think we should keep the existing behavior.\r\n\r\n> In a browser, users can append `.json` to the request URL to force HTTP Basic.\r\n\r\nThis doesn't seem too onerous for the user, and given that preemptive HTTP Basic is supported for any accept type I don't see us breaking a lot of real API users.",
      "id":10907,
      "updated_at":"03 November, 2017"
    },
     {
      "author":"Phil Webb",
      "body":"Actually it appears that adding `.json` as an extension isn't supported by actuator.",
      "id":10907,
      "updated_at":"04 November, 2017"
    },
    {
      "author":"Dave Syer",
      "body":"I don't know if we need to change the new defaults, but I do think we need a way for hapless users (me) to become better informed about how things work. Maybe I'm looking in the wrong place, but it seems like the user guide doesn't reflect any of the above discussion (or the related discussion in #10306), and the frustration comes not when browsing a user guide, but in the trenches running apps in an IDE and being baffled by changes that are hard to understand.\r\n\r\nKnowing that thing about \"accept type that does not include HTML\" could be very important. Better \"deprecation\" docs on existing 1.x configuration properties might also help, since some users will stumble on the changes in the IDE and configuration properties.",
      "id":10907,
      "updated_at":"06 November, 2017"
    },
    {
      "author":"Andy Wilkinson",
      "body":"> Actually it appears that adding .json as an extension isn't supported by actuator.\r\n\r\nThat's to avoid problems with the URL triggering unwanted content negotiation. See https://github.com/spring-projects/spring-boot/issues/8765 for details. If we want `.json` to work as @rwinch has described then I think we'd need to rework all of the actuator's endpoints to guarantee that the URL's path will never end with something that could be mistaken for a path extension.",
      "id":10907,
      "updated_at":"06 November, 2017"
    }]