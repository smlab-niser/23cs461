---
marp: true
# theme: default
# theme: gaia
theme: uncover
class:
  - invert
  - lead
style: |
  p {
    font-size: 35px;
    text-align: left;
    text-align: justify;
  }

  li{
    font-size: 30px;
  }

  h1 {
    font-size: 70px;
    text-align: center;
  }
title: "Aligning benchmark datasets for TSR"
author: "Aritra Mukhopadhyay"
date: "2023-08-3"
description: "Made this slide to "


header: "Aligning benchmark datasets for TSR"
_header: ""
footer: "Aritra Mukhopadhyay"
_footer: ""
paginate: false
_paginate: false
color: white
backgroundColor: #16181E
# size: 4:3
---

# **Neural Networks at a Fraction:** Table Structure Recognition

<br>
<p style="text-align:center"><a href="https://peithonking.github.io/portfolio-page/">Aritra Mukhopadhyay</a></p>

---

## Objective

To make quaternion versions of the Table Transformer (TATR) model and deploy in a low powered mobile device with limited memory and computational power.
<br>
**Dataset:** PubTables-1M, FinTabNet, ICDAR 2013
**Model:** Table Transformer (TATR) model

---

## Relevant Papers

- [End-to-End Object Detection with Transformers (2020)](https://scontent-ccu1-1.xx.fbcdn.net/v/t39.2365-6/154305880_816694605586461_2873294970659239190_n.pdf?_nc_cat=108&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=DkHwrRBBc_cAX-eMpS7&_nc_ht=scontent-ccu1-1.xx&oh=00_AfCVQywPZJ9qTTMxk3f6OzsXUEBE9ASe4JMTKI1zE1gCqQ&oe=64F07EC3)
  from *Facebook AI Research (Nicolas Carion, Francisco Massa et al.)*
- [GriTS: Grid table similarity metric for table structure recognition](https://arxiv.org/pdf/2203.12555)
  from *Microsoft Research (Brandon Smock, Rohith Pesala, Robin Abraham)* (2022)
- [Aligning benchmark datasets for table structure recognition](https://arxiv.org/pdf/2303.00716)
  from *Microsoft Research (Brandon Smock, Rohith Pesala, Robin Abraham)* (2023)

---

## Plans Befor Midterm

- 🗸 Understand the GriTS metrics
- 🗸 Learn about transformers
- 🗸 Understand the DE:TR model and pipeline
- ▢ Understand the TATR model and dataset
- ▢ LTH on pretrained TATR on the FinTabNet dataset
- ▢ Compare Finetuned pruned model vs pruned finetuned model

---

## Plans After midterm

- ▢ Make quaternion version of the TATR model
- ▢ LTH on Quaternion TATR model
- ▢ Production
  - ▢ Export model weights in required format
  - ▢ Deploy on Microsoft Lens