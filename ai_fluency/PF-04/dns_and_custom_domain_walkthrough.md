# A Custom Domain for My ML Work Site: What I Would Configure and Why

**Assignment:** `PF-04`  
**Author:** Umer Sajid  
**Date:** August 14, 2026  
**Current live URL:** <https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/>

> **Status note:** The ML Work site is publicly live on a Vercel default URL. I have not bought or configured a custom domain, so this is a learning walkthrough, not a claim that a custom DNS configuration is already live.

## Domain and hosting are different jobs

A **domain** is the human-readable address people type, such as `example.com`. **Hosting** is the service that stores and serves the HTML, CSS, images, and application responses behind that address. I would buy or register a domain through a registrar, keep control of the account and renewal settings, and choose a hosting provider for the deployed site. The two can be from different companies: a registrar can manage the domain while Vercel hosts the project.

The public ML Work site currently uses Vercel as the host. If I later choose a domain such as `umersajid.dev` (only if it is available and I decide to purchase it), I would add it to the existing Vercel project. Vercel would then tell me exactly which DNS records it expects before it can verify ownership and route visitors to the project. That separation is useful: changing page content would still be a Git deployment, while changing where the domain points would happen in DNS.

## DNS in plain language

**DNS** is the Internet’s address book. It translates a name such as `www.example.com` into the destination needed to reach the correct service. A DNS provider stores a collection of records for a domain, and each record type has a different job. Cloudflare’s documentation describes records as the information that makes a website or application available to visitors; the common fields are record type, name, content, and TTL. [1]

When a visitor opens a custom domain, their device asks a DNS resolver for the record. The resolver finds the domain’s authoritative nameservers, gets the appropriate record, and returns a target so the browser can connect to the host. DNS updates can be cached for the record’s TTL, so a correct update might not appear everywhere immediately. The host then receives the request and serves the appropriate site. A CNAME is an alias from one domain name to another domain name—not directly to an IP address—so it is common for a subdomain such as `www` to point to a hosting provider’s target. [2]

## Nameservers and common records

**Nameservers** are the authoritative DNS servers that hold the records for a domain. The registrar normally lets the domain owner choose which nameservers are authoritative; changing nameservers delegates DNS control to another provider. An NS record identifies those authoritative servers, and multiple nameservers provide redundancy. [3]

| Record | Plain-language purpose | Example future use for an ML Work site |
|---|---|---|
| `A` | Points a hostname to an IPv4 address. | A provider might ask the apex domain (`@`) to point to a published IPv4 address. |
| `AAAA` | Points a hostname to an IPv6 address. | Used only if the host instructs me to add its IPv6 target. |
| `CNAME` | Makes one hostname an alias of another hostname. | `www` could point to the Vercel target Vercel shows for my project. |
| `TXT` | Stores short text for verification or policy. | Vercel may request a verification TXT record before it accepts a domain. |
| `MX` | Routes email for the domain. | Only needed if I later use domain-based email; it is separate from website hosting. |
| `NS` | Identifies the authoritative nameservers. | Updated only if I intentionally move DNS management to a different provider. |

A practical constraint is that a hostname with a CNAME cannot simultaneously have other record types at the same name under ordinary DNS rules. That matters when planning `www` or a subdomain: I would avoid adding a CNAME where an email, verification, or other required record already exists. [2]

## My first custom-domain plan, step by step

1. **Choose and register a domain intentionally.** I would select a name that matches my professional identity, check its renewal price and privacy options, and keep registrar access under my own control. I would not buy a name merely for this assignment.
2. **Keep the Vercel project as the host.** In Vercel, I would open the current ML Work project, go to its domain settings, and add the exact domain I registered. Vercel’s current documentation explains that a domain must be added and verified and that the needed DNS or nameserver values are shown in the project flow. [4]
3. **Use the host’s displayed record values exactly.** At the DNS provider, I would add the record Vercel asks for. For a subdomain this will commonly be a CNAME; for an apex domain it may be an A/AAAA record or provider-specific direction. I would not copy a generic IP address from an old tutorial, because provider targets can change.
4. **Verify ownership and wait for propagation.** I would use the Vercel verification status, then check with a DNS lookup and open the custom domain in a private browser window. I would expect caches to delay some resolvers rather than repeatedly changing records before the first change has propagated.
5. **Set one canonical address.** I would decide whether `www` or the root domain is primary, configure the other to redirect, and confirm HTTPS is active. I would test Home, Case study, About, Contact, and Notes at the final address.
6. **Preserve the current public URL during the change.** I would not delete the known working Vercel address until the custom domain has been verified and tested. The deployment source remains the Git repository’s `docs/` directory.

## Three provider paths I compared

| Hosting option | How I would connect a custom domain | Why I considered it | Decision |
|---|---|---|---|
| **Vercel** | Add the domain in Project Settings, then create the DNS record(s) Vercel shows and complete verification. [4] | The existing live site is already deployed here from the Git-linked repository. | **Chosen for now** to avoid an unnecessary migration. |
| **GitHub Pages** | Add the custom domain in Pages settings, create the needed DNS record at the registrar, then verify and enforce HTTPS. [5] | The site source is already on GitHub and is static. | A credible fallback if I later prefer GitHub-managed Pages. |
| **Netlify** | Add the domain in Domain management and either use Netlify DNS or configure the provider-specific external DNS records shown for the site. [6] | It is another suitable static-site host with clear domain tooling. | Not chosen because it would duplicate an already working deployment. |

## What I would test before calling it done

| Check | Why it matters |
|---|---|
| The root and chosen canonical URL resolve correctly | Confirms the DNS record points to the intended host. |
| HTTPS certificate is valid and no browser warning appears | Protects visitors and avoids an unprofessional first impression. |
| `www` and apex behavior is deliberate | Avoids two competing versions of the same site. |
| All five site pages load from the custom domain | Confirms host routing and relative links still work. |
| The case-study chart and public repository links load | Confirms the site’s evidence remains inspectable. |
| Mobile device opens the final custom address | Confirms the actual visitor path works beyond a local desktop preview. |

## Professional links and booking routes

The public site already links to the verified GitHub accounts and email route. I have **not** added a LinkedIn profile, CV download, booking calendar, or custom domain because no verified destination has been supplied. I will add each only after Umer provides the actual public URL or approved file; creating placeholder professional links would be misleading.

## Sources

[1]: https://developers.cloudflare.com/dns/manage-dns-records/ "Cloudflare — DNS records"
[2]: https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/ "Cloudflare — What is a DNS CNAME record?"
[3]: https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/ "Cloudflare — What is a DNS NS record?"
[4]: https://vercel.com/docs/domains/working-with-domains/add-a-domain "Vercel — Adding and configuring a custom domain"
[5]: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site "GitHub Docs — Managing a custom domain for a GitHub Pages site"
[6]: https://docs.netlify.com/manage/domains/configure-domains/configure-external-dns/ "Netlify Docs — Configure external DNS for a custom domain"
