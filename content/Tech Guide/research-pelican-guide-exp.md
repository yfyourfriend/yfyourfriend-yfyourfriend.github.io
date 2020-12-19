---
title: Creating your own site / blog / community (detailed)
date: 2020-07-20 10:41
slug: pelican-site-guide-exp
tags: tech, python, web
category: Tech Guide
summary: This article explores the choices involved in choosing and learning a static site generator, the prerequisites you shall need along the way, and what you can do to get there in an exploratory and detailed manner.  
---

This post was originally written as workshop material for fellow members of the 2020 NTU SPMS [Odyssey Research Programme](https://spms.ntu.edu.sg/Programmes/Undergrads/Odyssey/Pages/Research.aspx) undergraduate students.

A version of this blog entry with less detail and is hence easier for experienced reader is provided [here]({filename}/Tech Guide/research-pelican-guide.md).

On your first reading, especially, feel free to skim things.

> Often for beginners, it is easy to be drowned in "theory". But the goal of a programming is really to get things done. If you have the tendency to get hung over on these things: keep that in mind. Instead, focus on visualising the path and obstacles towards your goals: bit-wise information and the little installations and steps you need to get your first working website, and iteratively improve your understanding (and website) from there.


# The "big" idea!
	- Nevertheless, I am writing these out so you *know what you don't know* when following procedural guides. 

## Static Site Generators (Part 1)
- Websites can generally be classified into *static sites* and *dynamic sites*
	- [Dynamic sites](https://en.wikipedia.org/wiki/Dynamic_web_page)
	- [Static sites](https://en.wikipedia.org/wiki/Static_web_page)
	- Dynamic sites require a server etc; static sites are just *static* pages. It is easier for a layman to set up a static site for the purposes of a personal blog or a "researchers" blog as is the purpose in our use case. 
		- The dynamic site requires a separate server that actively responds to the users requests. The classic examples are your big e-commerce websites which need many more considerations like databases and security designed into them. 
		- Static sites are easier to maintain.
	- As we shall see, the use of static site generators in Python allows us to focus on the content and to get our messages out there into the world.

### Choices among various Python Static site generators
A note on technology choice in general: in the long run, it does not matter which you choose. As a beginner, pick one with good support from the community and master it first. When you are reach a certain level of proficiency, you then understand the nuances and realise it is not that hard to switch between languages or frameworks.

For me, the principle reason to choose **Pelican** over **Nikola**, which are both Static Site Generators in Python, is that Nikola is uglier with its theme of the box, and Pelican has nicer and easier to customise themes. This is related to the next point in which Pelican is simpler, in that I think Nikola has layers of complexity which are not as easy to break down when you find an error. 


## Static Site Generators (Part 2)
Here we show why it is worthwhile to learn a static site generator, as opposed to use other "free" tools like wordpress.

- You will be in complete control over all the files and content you produce. 
- You are not tied down to "upgrading" the service you have with the service provider. The increase use cases you have instead are unlocked as you upgrade yourself! That is, with understanding and working with the technology. 

Let us begin to get our hands dirty! 

# **Eventual** Prerequisites
- [Markdown](https://sourceforge.net/p/pelican-edt/wiki/markdown_syntax/)
	- Markdown is a lightweight content creation syntax designed for the web, simplifying pure HTML. 
	- Your content is written in either Markdown (.md) or reStructured Text (.rst), which are both just **text files** with different extensions, to let the machine know it can read and process your file in those particular ways. 
	- A guide to its syntax is provided in the link above.
		- Essentially, with markdown you are typing content almost as you would normally. When you need features such as bullet lists, embedding videos and so on, do refer to this link above, which provides a 'cheatsheet'.
	- You can alternatively choose to write [.rst](https://www.drpi.fr/en/blog/2020-04-01-pelican-rst-guide.html) over .md files.
		- In both cases, you could think of these "markup languages" as slight improvements over pure text.
		- Focus on content creation, and the rest of your static site generator creates machine-readable HTML/CSS for you. 
- Python
	- We assume a Python install on your system.
	- This guide will work out of the box for MacOs/Linux users
	- For beginners on **Windows**:
		- Most guides on the internet about Pelican and other Python tools are written from the perspective that you are somewhat familiar with Command Line tools ("CLI"; "I" for interface).
			- [Here's what microsoft says about Python installs on Windows](https://docs.microsoft.com/en-us/windows/python/beginners)
				- Microsoft suggests Python users in these use cases, Pelican included, to use the Windows Subsystem for Linux (WSL).
		- If you have an existing install of the Anaconda Distribution on Windows, [this](https://pythonforundergradengineers.com/how-i-built-this-site-1.html) is a fairly detailed guide for you, which you can use along side or in replacement of this side.
			- In any case, the provided guide is very procedural, which is why I wrote this guide to explain the 'why"s involved. 

# Get inspired! 

Examples which are written in Pelican! The websites are all available here, as are their accompanying source codes. 

## Official pelican themes
- http://www.pelicanthemes.com/

## Examples I like
- https://canuxcheng.com/
	- https://github.com/crazy-canux/blog_pelican
	- nice tagging system
- https://sagar.se/ 
	- https://github.com/sagarbehere/sagar.se
	- fully featured as in: blog, projects, publications, cv, tags, categories, contact ... 
- https://fuller.li/
	- modern look (minimalistic page)

- https://www.matthewgraybosch.com/
	- currently very very minimalist
	- if you dig with git history / wayback archive; used to be v fully featured, search engine etc. theres a custom theme

- https://github.com/talha131/onCrashReboot
	- Clean and fully functional
		- search
		- tags
		- cv

These are ["open source"](https://en.wikibooks.org/wiki/FOSS_A_General_Introduction/Introduction) in that it allows beginners or budding humans at any level to build on existing code, much like a certain inclination towards the [*freedom of knowledge* and academia.](http://custodians.online/)

Viewing the files at *github*, an open source version control repository, is essentially peaking under the hood of these websites. Find ones you fancy and remember them. 

# Your first steps
Your first step is really to install Pelican. As above, I will defer the reader to their preferred python installation, and leave this link [https://realpython.com/installing-python/](https://realpython.com/installing-python/) for the uninitiated. If you are completely new to Python, I would recommend checking out some famous free online course or famous book. 

I prefer to start with [the official Quickstart guide](https://docs.getpelican.com/en/stable/quickstart.html#preview-your-site). I'll wait here as I assume you'll follow it: there you would learn how to install pelican with **pip**, the defacto python package manager. You're strongly encouraged to use a virtual environment. 

Check out some [other guides](https://snipcart.com/blog/pelican-blog-tutorial-search-comments) too for more long-windedness. 

# Next steps
You have a content folder which contains all your posts

running: 

> pelican content

will compile all your Markdown/reStructured text files into an "output" folder. This is pure HTML/CSS. 

> pelican -l

will allow you to locally view your website, using this output folder.

Most high-level settings are easily toggled by editing the *text file* (this is a theme in Linux / the open source computing world!) called **pelicanconf.py** and later on, **publishconf.py**. Your go to source is always the [official documentation(s)](https://docs.getpelican.com/en/stable/#) alongside any helpful guide. 

- Your next steps, which can be done concurrently are the following
	- Produce more content in markdown/rst
		- these will be independent of any theme you choose, or even any static site generator or web service you choose.
	- Find or imagine a theme you like, and work towards actualising it.
	- Publishing on Github Pages
		- https://opensource.com/article/19/5/run-your-blog-github-pages-python
		- https://medium.com/@acalamea/step-by-step-guide-to-setup-a-web-site-using-pelican-and-gitpages-5de976ae44cb

# Getting a theme you like
You need to install themes you like, by browsing http://www.pelicanthemes.com/ and https://github.com/getpelican/pelican/wiki/Powered-by-Pelican, which was where I shortlisted my exmplar blogs from. 

## Getting further with your custom themes
Starting with some template as a base, learn how to edit your own theme https://docs.getpelican.com/en/stable/themes.html

# Conclusion
Learning pelican as a static site generator allows you to take complete ownership of your content. Importantly, learning to take control of this environment is also the process of becoming used to a little bit of programming - you cultivate the general ability


