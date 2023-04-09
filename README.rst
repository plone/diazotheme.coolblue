This repository is archived and read only.

If you want to unarchive it, then post to the [Admin & Infrastructure (AI) Team category on the Plone Community Forum](https://community.plone.org/c/aiteam/55).

Introduction
============

This package contains the new Plone Diazo based theme. This package also takes
care of overriding plone templates for cleanup of un-styled plone (using jbot,
changes need to be roled back into all the other packages at a suitable time).
This package also contains minimal styling for un-styled plone which will not
be applied when Diazo is.

In docs/TODO.txt there is a list of tasks that need to be done.

Setup of the package
--------------------
The project is currently setup as follows:

browser
    Contains the minimal styling for un-styled Plone
    (to be rolled into Products.CMFPlone)
profiles
    Contains the profiles to set up the minimal styling and the skins folder
    (to be rolled into Products.CMFPlone)
skins
    Contains some resources that are currently hard to override throught jbot.
    (to be rolled into Products.CMFPlone)
clean
    Contains a ultra-minimal theme only to check styles with and without
    Diazo applied. (Can be purged/removed after initial development)
coolblue
    Contains the new plonetheme based on Oriols designs (docs/design)
templates
    All the jbot templates, already subdivided for better overview.

    browser
        For overriding browser view templates which are not viewlets.
    portlets
        For overriding portlets
    skins
        For overriding old-style skin templates, though this should stay near
        empty because of skins removal efforts.
    viewlets
        For overriding viewlets (was a huge chunk already so better split them
        off)

Objectives
----------

**Templates, markup and styles**

- Clean all useless old markup from the base plone templates. Whatever you
  need for theming can be added through Diazo.
- Add classes to markup that only contain id's, do not use id's in CSS and
  adhere to OOCSS practices.

**Theme**

- Get minimal styling onto un-styled Plone to be able to use it with the
  theme editor. Control panels should end up in p.a.toolbar and should not
  be focused on.
- New theme based on Oriols designs. Set it up so it is easily customized
  and uses as little styles as possible. The more lightweight the better.
  It uses PureCSS to have the basics styled sufficiently.
- Add icon fonts to be pixel independent.
- Add SVG logo to be pixel independent.
