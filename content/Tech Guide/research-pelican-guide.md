---
title: Creating your own site / blog in Pelican
date: 2020-07-20 10:41
slug: pelican-site-guide
tags: tech, python, web
category: Tech Guide
summary: A guide to setting up your own blog with Pelican
---

This post was originally written as workshop material for fellow members of the 2020 NTU SPMS [Odyssey Research Programme](https://spms.ntu.edu.sg/Programmes/Undergrads/Odyssey/Pages/Research.aspx) undergraduate students. This handout is then for audiences who are relatively versed with what Pelican or other Static site generators can do and would be able to pick it up with some crucial links and hints. 

A version of this blog entry with more detail intended for persons who are newer to programming or are self-learning and would like to work with more detail [here]({filename}/Tech Guide/research-pelican-guide-exp.md).


# The "big" idea!
	- Nevertheless, I am writing these out so you *know what you don't know* when following procedural guides. 

## Static Site Generators (Part 1)
- Websites can generally be classified into *static sites* and *dynamic sites*
	- [Dynamic sites](https://en.wikipedia.org/wiki/Dynamic_web_page)
	- [Static sites](https://en.wikipedia.org/wiki/Static_web_page)

### Choices among various Python Static site generators
For me, the principle reason to choose **Pelican** over **Nikola**, which are both Static Site Generators in Python, is that Nikola is uglier with its theme of the box, and Pelican has nicer and easier to customise themes. This is related to the next point in which Pelican is simpler, in that I think Nikola has layers of complexity which are not as easy to break down when you find an error. 


## Static Site Generators (Part 2)
Here we show why it is worthwhile to learn a static site generator, as opposed to use other "free" tools like wordpress.

- You will be in complete control over all the files and content you produce. 
- You are not tied down to "upgrading" the service you have with the service provider. The increase use cases you have instead are unlocked as you upgrade yourself! That is, with understanding and working with the technology. 

Let us begin to get our hands dirty! 

# **Eventual** Prerequisites
- [Markdown](https://sourceforge.net/p/pelican-edt/wiki/markdown_syntax/)
- Python
	- We assume a Python install on your system.
	- This guide will work out of the box for MacOs/Linux users
	- For users on **Windows**:
		- Most guides on the internet about Pelican and other Python tools are written from the perspective that you are somewhat familiar with Command Line tools ("CLI"; "I" for interface).
			- [Here's what microsoft says about Python installs on Windows](https://docs.microsoft.com/en-us/windows/python/beginners)
				- Microsoft suggests Python users in these use cases, Pelican included, to use the Windows Subsystem for Linux (WSL).
		- If you have an existing install of the Anaconda Distribution on Windows, [this](https://pythonforundergradengineers.com/how-i-built-this-site-1.html) is a fairly detailed guide for you, which you can use along side or in replacement of this guide.
			- In any case, the provided guide is very procedural, which is why I wrote this guide to explain the 'why"s involved. 
- Git
- If interested in self-theming:
	- Jinja2 is simple to understand as a templating language that works over CSS and HTML. Thereafter, your usual HTML skills go along way since HTML elements like "span" and class-based styling can be applied almost anywhere.

- Once you understand Pelican on a macro level, you are good! Look at the [official documentation]( https://docs.getpelican.com/en/stable/), imagine what you want and zone into those

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
Learning pelican as a static site generator allows you to take complete ownership of your content. Importantly, learning to take control of this environment is also the process of becoming used to a little bit of programming - you cultivate the general ability to work with new libraries. 


