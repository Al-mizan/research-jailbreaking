import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Colors
    C_BG = RGBColor(248, 250, 252)         # Slate 50
    C_CARD_BG = RGBColor(255, 255, 255)    # White
    C_CARD_BORDER = RGBColor(226, 232, 240) # Slate 200
    C_PRIMARY = RGBColor(15, 23, 42)       # Slate 900
    C_SECONDARY = RGBColor(30, 41, 59)     # Slate 800
    C_MUTED = RGBColor(100, 116, 139)      # Slate 500
    C_BODY = RGBColor(51, 65, 85)          # Slate 700

    C_NAVY_DARK = RGBColor(11, 19, 43)     # Slate/Navy 950
    C_NAVY_ACCENT = RGBColor(30, 58, 138)  # Blue 900
    C_BLUE = RGBColor(37, 99, 235)         # Blue 600
    C_BLUE_LIGHT = RGBColor(239, 246, 255) # Blue 50
    C_BLUE_BORDER = RGBColor(191, 219, 254)# Blue 200

    C_RED = RGBColor(220, 38, 38)          # Red 600
    C_RED_LIGHT = RGBColor(254, 242, 242)  # Red 50
    C_RED_BORDER = RGBColor(254, 202, 202) # Red 200

    C_GREEN = RGBColor(5, 150, 105)        # Emerald 600
    C_GREEN_LIGHT = RGBColor(236, 253, 245)# Emerald 50
    C_GREEN_BORDER = RGBColor(167, 243, 208)# Emerald 200

    C_AMBER = RGBColor(217, 119, 6)        # Amber 600
    C_AMBER_LIGHT = RGBColor(254, 243, 199)# Amber 50
    C_AMBER_BORDER = RGBColor(253, 230, 138)# Amber 200

    FONT_HEAD = "Arial"
    FONT_BODY = "Arial"

    def set_slide_bg(slide, color=C_BG):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, category, title, subtitle=""):
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.40), Inches(3.2), Inches(0.30))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_BLUE_LIGHT
        badge.line.color.rgb = C_BLUE_BORDER
        badge.line.width = Pt(1)
        tf = badge.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.02)
        tf.margin_bottom = Inches(0.02)
        tf.margin_left = Inches(0.1)
        tf.margin_right = Inches(0.1)
        p = tf.paragraphs[0]
        p.text = category.upper()
        p.font.name = FONT_HEAD
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = C_BLUE
        p.alignment = PP_ALIGN.CENTER
        
        tx = slide.shapes.add_textbox(Inches(0.8), Inches(0.76), Inches(11.733), Inches(0.85))
        tf2 = tx.text_frame
        tf2.word_wrap = True
        tf2.margin_left = 0
        tf2.margin_top = 0
        tf2.margin_right = 0
        tf2.margin_bottom = 0
        
        p2 = tf2.paragraphs[0]
        p2.text = title
        p2.font.name = FONT_HEAD
        p2.font.size = Pt(21)
        p2.font.bold = True
        p2.font.color.rgb = C_PRIMARY
        
        if subtitle:
            p3 = tf2.add_paragraph()
            p3.text = subtitle
            p3.font.name = FONT_BODY
            p3.font.size = Pt(11)
            p3.font.color.rgb = C_MUTED
            p3.space_before = Pt(3)

    def add_footer(slide, slide_num, total_slides=16):
        tx1 = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(9.5), Inches(0.3))
        tf1 = tx1.text_frame
        tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = 0
        p1 = tf1.paragraphs[0]
        p1.text = "Research Seminar: AI Agent Supply-Chain Security & Multilingual Jailbreaking  |  Supervisor Briefing"
        p1.font.name = FONT_BODY
        p1.font.size = Pt(9)
        p1.font.color.rgb = C_MUTED
        
        tx2 = slide.shapes.add_textbox(Inches(10.5), Inches(7.05), Inches(2.033), Inches(0.3))
        tf2 = tx2.text_frame
        tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = 0
        p2 = tf2.paragraphs[0]
        p2.text = f"Slide {slide_num} of {total_slides}"
        p2.font.name = FONT_BODY
        p2.font.size = Pt(9)
        p2.font.bold = True
        p2.font.color.rgb = C_MUTED
        p2.alignment = PP_ALIGN.RIGHT

    def add_card(slide, left, top, width, height, bg_color=C_CARD_BG, border_color=C_CARD_BORDER, border_width=1):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(border_width)
        return card

    def add_stat_box(slide, left, top, width, height, num_str, label_str, subtext="", color=C_BLUE):
        card = add_card(slide, left, top, width, height, bg_color=C_CARD_BG, border_color=C_CARD_BORDER)
        tx = slide.shapes.add_textbox(left + Inches(0.08), top + Inches(0.08), width - Inches(0.16), height - Inches(0.16))
        tf = tx.text_frame
        tf.word_wrap = True
        tf.margin_top = 0
        tf.margin_left = 0
        tf.margin_right = 0
        tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = num_str
        p.font.name = FONT_HEAD
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = color
        p.alignment = PP_ALIGN.CENTER
        
        p2 = tf.add_paragraph()
        p2.text = label_str
        p2.font.name = FONT_HEAD
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = C_PRIMARY
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(2)
        
        if subtext:
            p3 = tf.add_paragraph()
            p3.text = subtext
            p3.font.name = FONT_BODY
            p3.font.size = Pt(8.5)
            p3.font.color.rgb = C_MUTED
            p3.alignment = PP_ALIGN.CENTER
            p3.space_before = Pt(2)

    def add_bullet(tf, bold_prefix, text, pt_size=10.5, text_color=C_BODY, space_above=5):
        p = tf.add_paragraph()
        p.font.name = FONT_BODY
        p.font.size = Pt(pt_size)
        p.space_before = Pt(space_above)
        run_bold = p.add_run()
        run_bold.text = "•  " + bold_prefix + ": " if bold_prefix else "•  "
        run_bold.font.bold = True
        run_bold.font.color.rgb = C_PRIMARY
        run_body = p.add_run()
        run_body.text = text
        run_body.font.color.rgb = text_color

    # ==========================================
    # SLIDE 1: Title Slide (Modern Dark Slate/Navy)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1, C_NAVY_DARK)
    
    # Decorative accent line
    acc_line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(1.2), Inches(1.5), Inches(0.08))
    acc_line.fill.solid()
    acc_line.fill.fore_color.rgb = C_BLUE
    acc_line.line.fill.background()

    # Category badge
    t_box = s1.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(10.9), Inches(4.5))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    
    p_badge = tf1.paragraphs[0]
    p_badge.text = "RESEARCH SEMINAR & SUPERVISOR BRIEFING"
    p_badge.font.name = FONT_HEAD
    p_badge.font.size = Pt(12)
    p_badge.font.bold = True
    p_badge.font.color.rgb = RGBColor(147, 197, 253) # Light Blue 300
    
    p_title = tf1.add_paragraph()
    p_title.text = "Frontier Vulnerabilities in Autonomous AI Systems"
    p_title.font.name = FONT_HEAD
    p_title.font.size = Pt(32)
    p_title.font.bold = True
    p_title.font.color.rgb = RGBColor(255, 255, 255)
    p_title.space_before = Pt(12)
    
    p_sub = tf1.add_paragraph()
    p_sub.text = "A Critical Synthesis of Agentic Supply-Chain Exploits & Cross-Lingual Safety Alignment Failures"
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = RGBColor(203, 213, 225) # Slate 300
    p_sub.space_before = Pt(10)

    # 2 Pillar badges on title
    c_p1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(4.5), Inches(5.2), Inches(1.4))
    c_p1.fill.solid()
    c_p1.fill.fore_color.rgb = RGBColor(15, 23, 42)
    c_p1.line.color.rgb = RGBColor(51, 65, 85)
    tf_p1 = c_p1.text_frame
    tf_p1.word_wrap = True
    tf_p1.margin_top = Inches(0.12)
    tf_p1.margin_left = Inches(0.2)
    p = tf_p1.paragraphs[0]
    p.text = "Domain 1: Agentic Supply Chains & Tool Hijacking"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(96, 165, 250)
    p2 = tf_p1.add_paragraph()
    p2.text = "• Model Context Protocol (MCP) tool poisoning\n• Semantic registry manipulation (SKILL.md)\n• Automated two-channel injection (SkillJect)"
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_before = Pt(4)

    c_p2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.5), Inches(5.3), Inches(1.4))
    c_p2.fill.solid()
    c_p2.fill.fore_color.rgb = RGBColor(15, 23, 42)
    c_p2.line.color.rgb = RGBColor(51, 65, 85)
    tf_p2 = c_p2.text_frame
    tf_p2.word_wrap = True
    tf_p2.margin_top = Inches(0.12)
    tf_p2.margin_left = Inches(0.2)
    p = tf_p2.paragraphs[0]
    p.text = "Domain 2: Multilingual Safety & Jailbreak Generalization"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(52, 211, 153) # Emerald 400
    p2 = tf_p2.add_paragraph()
    p2.text = "• Cross-lingual safety asymmetry (10 languages)\n• Multi-turn low-resource African language attacks\n• The Translation Quality Fallacy & human red-teaming"
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_before = Pt(4)

    # Metadata footer on title
    tx_meta = s1.shapes.add_textbox(Inches(1.2), Inches(6.3), Inches(10.9), Inches(0.5))
    tf_meta = tx_meta.text_frame
    p_meta = tf_meta.paragraphs[0]
    p_meta.text = "Comprehensive Literature Review & Strategic Synthesis  |  5 Frontier Papers (2025–2026)  |  September 2026"
    p_meta.font.size = Pt(10)
    p_meta.font.color.rgb = RGBColor(148, 163, 184)

    # ==========================================
    # SLIDE 2: Executive Summary & The Dual Paradigm Shift
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "Executive Overview", "The Dual Paradigm Shift in LLM and Agent Security", 
               "How autonomous tool agency and multilingual deployment dismantle conventional LLM safety assumptions")
    add_footer(s2, 2)

    # 2 Big Cards
    c1 = add_card(s2, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.9))
    tf_c1 = c1.text_frame
    tf_c1.word_wrap = True
    tf_c1.margin_left = Inches(0.25)
    tf_c1.margin_right = Inches(0.25)
    tf_c1.margin_top = Inches(0.25)
    p = tf_c1.paragraphs[0]
    p.text = "Theme 1: The Semantic & Tool Supply Chain"
    p.font.name = FONT_HEAD
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK
    
    add_bullet(tf_c1, "From Chat to Action", "Agents no longer merely generate text; they autonomously search registries, load third-party skills, and execute shell commands and APIs.", 10.5)
    add_bullet(tf_c1, "Documentation as Code", "Natural language instructions (SKILL.md, MCP tool schemas) act as operational code shaping retrieval, selection, and runtime execution.", 10.5)
    add_bullet(tf_c1, "Broken Trust Boundaries", "Server-provided metadata flows directly into the agent reasoning loop with zero static validation across most clients.", 10.5)
    add_bullet(tf_c1, "Real-World Attack Impact", "Credential exfiltration (.env), silent telemetry logging, phishing generation, and arbitrary Remote Code Execution (RCE).", 10.5)

    c2 = add_card(s2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    tf_c2 = c2.text_frame
    tf_c2.word_wrap = True
    tf_c2.margin_left = Inches(0.25)
    tf_c2.margin_right = Inches(0.25)
    tf_c2.margin_top = Inches(0.25)
    p = tf_c2.paragraphs[0]
    p.text = "Theme 2: Cross-Lingual Alignment Fragility"
    p.font.name = FONT_HEAD
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK
    
    add_bullet(tf_c2, "English Alignment Bias", "Frontier safety tuning (RLHF/DPO) is overwhelmingly optimized on high-resource English datasets, creating linguistic blindspots.", 10.5)
    add_bullet(tf_c2, "The Safety-Capability Paradox", "High-resource languages resist standard harmful prompts but become hyper-vulnerable to adversarial optimization due to high linguistic proficiency.", 10.5)
    add_bullet(tf_c2, "The Translation Quality Fallacy", "Automated benchmarks falsely label low-resource languages as 'safe' because machine translation mangles prompt semantics.", 10.5)
    add_bullet(tf_c2, "Multi-Turn Conversational Exploit", "Single-turn attacks are caught by basic filters, but multi-turn pacing bypasses guardrails across commercial frontier LLMs.", 10.5)

    # ==========================================
    # SLIDE 3: Theoretical Grounding & Tripartite Trust Model
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "Theoretical Framework", "System Architecture & Canonical Threat Modeling", 
               "Grounding vulnerabilities in the tripartite system model of autonomous agents (CONTEXT.md)")
    add_footer(s3, 3)

    # 3 Column Cards
    col_w = Inches(3.7)
    gap = Inches(0.3)
    
    # Col 1: Planes
    col1 = add_card(s3, Inches(0.8), Inches(1.8), col_w, Inches(4.9))
    tf_col1 = col1.text_frame
    tf_col1.word_wrap = True
    tf_col1.margin_left = Inches(0.2)
    tf_col1.margin_right = Inches(0.2)
    tf_col1.margin_top = Inches(0.2)
    p = tf_col1.paragraphs[0]
    p.text = "The Three Execution Planes"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_BLUE
    add_bullet(tf_col1, "Control Plane", "Privileged channel comprising developer system prompts, safety guardrails, and authenticated user directives.", 10)
    add_bullet(tf_col1, "Reasoning Plane", "Intermediate state space where the agent plans, decomposes goals, maintains scratchpads, and executes ReAct loops.", 10)
    add_bullet(tf_col1, "Data Plane", "Untrusted channel carrying tool outputs, retrieved documents, external skills, and API responses.", 10)
    add_bullet(tf_col1, "The Flaw", "Control-Data Conflation occurs when the LLM treats untrusted Data Plane inputs as Control Plane instructions.", 10)

    # Col 2: Vulnerability Mechanisms
    col2 = add_card(s3, Inches(0.8) + col_w + gap, Inches(1.8), col_w, Inches(4.9))
    tf_col2 = col2.text_frame
    tf_col2.word_wrap = True
    tf_col2.margin_left = Inches(0.2)
    tf_col2.margin_right = Inches(0.2)
    tf_col2.margin_top = Inches(0.2)
    p = tf_col2.paragraphs[0]
    p.text = "Core Exploit Mechanisms"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_RED
    add_bullet(tf_col2, "Confused Deputy", "An agent with high system privileges is coerced by third-party metadata into executing malicious actions.", 10)
    add_bullet(tf_col2, "Tool Hijacking", "Coercing tool invocation with attacker-controlled arguments, altering local state or exfiltrating data.", 10)
    add_bullet(tf_col2, "Scratchpad Pollution", "Transient corruption of working memory or chain-of-thought during an active execution turn.", 10)
    add_bullet(tf_col2, "Episodic & Semantic Poisoning", "Injecting instructions that persist across chat sessions or poison long-term vector memory stores.", 10)

    # Col 3: Adversary Profiles
    col3 = add_card(s3, Inches(0.8) + (col_w + gap)*2, Inches(1.8), col_w, Inches(4.9))
    tf_col3 = col3.text_frame
    tf_col3.word_wrap = True
    tf_col3.margin_left = Inches(0.2)
    tf_col3.margin_right = Inches(0.2)
    tf_col3.margin_top = Inches(0.2)
    p = tf_col3.paragraphs[0]
    p.text = "Adversary Taxonomy"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_AMBER
    add_bullet(tf_col3, "Passive Adversary", "Implants static payloads in external registries (ClawHub, MCP servers) awaiting autonomous ingestion by agents.", 10)
    add_bullet(tf_col3, "Active Adversary", "Interacts dynamically across multi-turn dialogs, adapting prompts based on model output to bypass safety filters.", 10)
    add_bullet(tf_col3, "Closed-Loop Adversary", "Employs an automated multi-agent attack loop that analyzes runtime execution traces to iteratively optimize payloads.", 10)
    add_bullet(tf_col3, "Collusive Adversary", "Coordinates external untrusted data with an internal user to systematically evade sandbox controls.", 10)

    # ==========================================
    # SLIDE 4: Section Divider - Theme 1
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4, C_NAVY_DARK)
    
    t_box4 = s4.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(10.9), Inches(4.0))
    tf4 = t_box4.text_frame
    tf4.word_wrap = True
    
    p = tf4.paragraphs[0]
    p.text = "THEME 1: AGENT SKILLS & TOOL SUPPLY-CHAIN ATTACKS"
    p.font.name = FONT_HEAD
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RGBColor(96, 165, 250)
    
    p2 = tf4.add_paragraph()
    p2.text = "Evaluating MCP Protocols, Skill Registries, and Automated Injection"
    p2.font.name = FONT_HEAD
    p2.font.size = Pt(28)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(255, 255, 255)
    p2.space_before = Pt(10)
    
    p3 = tf4.add_paragraph()
    p3.text = "A deep examination of three breakthrough papers analyzing how third-party tools, natural-language documentation, and registry-facing lifecycles compromise autonomous AI agents."
    p3.font.name = FONT_BODY
    p3.font.size = Pt(13)
    p3.font.color.rgb = RGBColor(203, 213, 225)
    p3.space_before = Pt(10)

    # 3 paper cards
    c_p1 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(4.5), Inches(3.4), Inches(1.6))
    c_p1.fill.solid()
    c_p1.fill.fore_color.rgb = RGBColor(15, 23, 42)
    c_p1.line.color.rgb = RGBColor(51, 65, 85)
    tf = c_p1.text_frame
    tf.word_wrap = True
    tf.margin_top = Inches(0.15)
    tf.margin_left = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Paper 1: MCP Security"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(147, 197, 253)
    p2 = tf.add_paragraph()
    p2.text = "Huang et al. (2026)\nThreat modeling & client-side tool poisoning in 7 MCP clients."
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = RGBColor(226, 232, 240)

    c_p2 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.9), Inches(4.5), Inches(3.4), Inches(1.6))
    c_p2.fill.solid()
    c_p2.fill.fore_color.rgb = RGBColor(15, 23, 42)
    c_p2.line.color.rgb = RGBColor(51, 65, 85)
    tf = c_p2.text_frame
    tf.word_wrap = True
    tf.margin_top = Inches(0.15)
    tf.margin_left = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Paper 2: Under SKILL.md"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(147, 197, 253)
    p2 = tf.add_paragraph()
    p2.text = "Saha et al. (2026)\nSemantic lifecycle attacks: Discovery, Selection, Governance."
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = RGBColor(226, 232, 240)

    c_p3 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.6), Inches(4.5), Inches(3.5), Inches(1.6))
    c_p3.fill.solid()
    c_p3.fill.fore_color.rgb = RGBColor(15, 23, 42)
    c_p3.line.color.rgb = RGBColor(51, 65, 85)
    tf = c_p3.text_frame
    tf.word_wrap = True
    tf.margin_top = Inches(0.15)
    tf.margin_left = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Paper 3: SkillJect"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(147, 197, 253)
    p2 = tf.add_paragraph()
    p2.text = "Jia et al. (2026)\nTwo-channel injection & trace-driven closed-loop optimization."
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = RGBColor(226, 232, 240)

    # ==========================================
    # SLIDE 5: Paper 1 Deep Dive - MCP Threat Modeling (Huang et al.)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "Paper 1 Deep Dive", "Model Context Protocol: Client-Side Tool Poisoning", 
               "Huang et al. (NYIT) — arXiv:2603.22489 | STRIDE/DREAD Analysis across 7 Commercial & OSS MCP Clients")
    add_footer(s5, 5)

    # Stat boxes
    add_stat_box(s5, Inches(0.8), Inches(1.8), Inches(2.7), Inches(1.15), "50+", "Identified Threats", "STRIDE/DREAD modeling", C_NAVY_ACCENT)
    add_stat_box(s5, Inches(3.8), Inches(1.8), Inches(2.7), Inches(1.15), "0% - 100%", "ASR Variance", "Claude Desktop vs Cursor", C_RED)
    add_stat_box(s5, Inches(6.8), Inches(1.8), Inches(2.7), Inches(1.15), "5 / 7", "Unvalidated Clients", "Zero static metadata validation", C_AMBER)
    add_stat_box(s5, Inches(9.8), Inches(1.8), Inches(2.7), Inches(1.15), "4 Attack Vectors", "Empirical Evaluation", "Files, Logging, Phish, RCE", C_BLUE)

    # 2 Detail Cards
    c1 = add_card(s5, Inches(0.8), Inches(3.15), Inches(5.7), Inches(3.6))
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Threat Modeling & Attack Methodology"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_PRIMARY
    add_bullet(tf, "Scope", "Evaluated 5 MCP components: Host+Client, LLM, MCP Server, External Stores, and Authorization Server.", 10)
    add_bullet(tf, "Highest Risk Vector", "Tool poisoning (embedding malicious prompts in tool descriptions/metadata) emerged as the most critical client vulnerability.", 10)
    add_bullet(tf, "4 Exploit Scenarios", "1) Reading sensitive files (.env / API keys); 2) Silently logging tool activity; 3) Injecting phishing links; 4) Remote Code Execution (RCE).", 10)
    add_bullet(tf, "Client Testbed", "Tested Claude Desktop, Cursor IDE, Cline, Continue, Gemini CLI, Claude Code, and Langflow in isolated Docker environments.", 10)

    c2 = add_card(s5, Inches(6.8), Inches(3.15), Inches(5.7), Inches(3.6))
    tf = c2.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Empirical Findings & Architectural Divide"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_PRIMARY
    add_bullet(tf, "The Security Divide", "Claude Desktop proved highly robust (Safe on 3/4 vectors). In contrast, Cursor was 100% Unsafe across all 4 attack categories.", 10)
    add_bullet(tf, "Human-in-the-Loop Illusion", "Clients with approval dialogs suffer from UI truncation (parameters hidden past horizontal view) and severe developer approval fatigue.", 10)
    add_bullet(tf, "Lack of Static Guardrails", "5 of 7 clients blindly ingest tool definitions without schema bounds checking or prompt-injection scanning.", 10)
    add_bullet(tf, "Key Limitation", "Evaluated controlled local versions; live production deployments and multi-server compositions remain open challenges.", 10)

    # ==========================================
    # SLIDE 6: Paper 2 Deep Dive - Under the Hood of SKILL.md (Saha et al.)
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_header(s6, "Paper 2 Deep Dive", "Semantic Supply-Chain Attacks on Agent Skill Registries", 
               "Saha et al. (UMD) — arXiv:2605.11418 | Manipulating the Pre-Execution Lifecycle: Discovery, Selection, Governance")
    add_footer(s6, 6)

    # Stat boxes
    add_stat_box(s6, Inches(0.8), Inches(1.8), Inches(3.7), Inches(1.15), "86.14%", "Discovery Win-Rate", "Manipulating OpenAI embedding retrieval", C_BLUE)
    add_stat_box(s6, Inches(4.8), Inches(1.8), Inches(3.7), Inches(1.15), "77.6%", "Selection Bias", "Agents pick attacker variant over benign", C_AMBER)
    add_stat_box(s6, Inches(8.8), Inches(1.8), Inches(3.7), Inches(1.15), "100%", "Governance Bypass", "Context overflow evades ClawScan", C_RED)

    # 3 Stage Cards
    col_w = Inches(3.7)
    gap = Inches(0.3)
    
    # Discovery
    c1 = add_card(s6, Inches(0.8), Inches(3.15), col_w, Inches(3.6))
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.18)
    p = tf.paragraphs[0]
    p.text = "1. Discovery Manipulation"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_BLUE
    add_bullet(tf, "Mechanism", "Appending short, optimized textual triggers to benign SKILL.md files to manipulate vector retrieval spaces.", 9.5)
    add_bullet(tf, "Performance", "86.14% win-rate and 80% Top-10 placement under OpenAI text-embedding-3-small.", 9.5)
    add_bullet(tf, "Real-World Impact", "In ClawHub realistic ranking (vector + BM25 + popularity), modified skills won 74.14% of trials.", 9.5)

    # Selection
    c2 = add_card(s6, Inches(0.8) + col_w + gap, Inches(3.15), col_w, Inches(3.6))
    tf = c2.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.18)
    p = tf.paragraphs[0]
    p.text = "2. Selection Manipulation"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_AMBER
    add_bullet(tf, "Mechanism", "Appending natural-language framing (assertive cues, false advertising) to description fields without altering functionality.", 9.5)
    add_bullet(tf, "Agent Preference", "Agents selected adversarial variants in 77.6% of paired trials across 100 ClawHub skills.", 9.5)
    add_bullet(tf, "Model Breakdown", "Qwen3-235B: 86.6%, Gemma-4-31B: 84.3%, GPT-5: 71.4%, GPT-4.1-mini: 68.2%.", 9.5)

    # Governance
    c3 = add_card(s6, Inches(0.8) + (col_w + gap)*2, Inches(3.15), col_w, Inches(3.6))
    tf = c3.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.18)
    p = tf.paragraphs[0]
    p.text = "3. Governance Evasion"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_RED
    add_bullet(tf, "Baseline", "Static rules + ClawScan LLM + VirusTotal caught 100% of direct malicious insertions.", 9.5)
    add_bullet(tf, "Semantic Evasion", "Paraphrasing allowed 73.9% of variants to avoid malicious blocks; Definition-of-Done (DoD) checklists avoided 66.3%.", 9.5)
    add_bullet(tf, "Window Overflow", "Placing instructions past the 10k character review truncation window yielded a 100% non-blocked bypass.", 9.5)

    # ==========================================
    # SLIDE 7: Paper 3 Deep Dive - SkillJect (Jia et al.)
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7)
    add_header(s7, "Paper 3 Deep Dive", "SkillJect: Automated Two-Channel Skill-Based Injection", 
               "Jia et al. (NTU, Oxford, et al.) — arXiv:2602.14211 | Decoupled Channels & Execution-Trace Optimization")
    add_footer(s7, 7)

    # Stat boxes
    add_stat_box(s7, Inches(0.8), Inches(1.8), Inches(2.7), Inches(1.15), "0.0%", "Naive Injection ASR", "Direct prompt insertion fails", C_GREEN)
    add_stat_box(s7, Inches(3.8), Inches(1.8), Inches(2.7), Inches(1.15), "80.7%", "SkillJect ASR", "Claude Code average across backends", C_RED)
    add_stat_box(s7, Inches(6.8), Inches(1.8), Inches(2.7), Inches(1.15), "80.5%", "OpenClaw ASR", "Consistent cross-platform exploit", C_RED)
    add_stat_box(s7, Inches(9.8), Inches(1.8), Inches(2.7), Inches(1.15), "4 Categories", "Evaluated Behaviors", "InfoDisc, PrivEsc, Write, Backdoor", C_NAVY_ACCENT)

    # 2 Detail Cards
    c1 = add_card(s7, Inches(0.8), Inches(3.15), Inches(5.7), Inches(3.6))
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Two-Channel Decoupled Architecture"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_PRIMARY
    add_bullet(tf, "The Core Dilemma", "Direct injection in SKILL.md is easily detected by safety filters or ignored by agents during task execution (0.0% ASR).", 10)
    add_bullet(tf, "Artifact Channel", "The actual malicious payload is concealed inside an auxiliary helper script (e.g. scripts/helper.py).", 10)
    add_bullet(tf, "Instruction Channel", "SKILL.md is rewritten with front-loaded inducement, framing script execution as an essential setup requirement with example commands.", 10)
    add_bullet(tf, "Confused Deputy Trigger", "The victim agent treats the script execution as a legitimate prerequisite before proceeding to the user task.", 10)

    c2 = add_card(s7, Inches(6.8), Inches(3.15), Inches(5.7), Inches(3.6))
    tf = c2.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Closed-Loop Multi-Agent Refinement"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_PRIMARY
    add_bullet(tf, "Tri-Agent Loop", "Attack Agent (GPT-3.5-Turbo) generates skills -> Sandboxed Victim Agent executes tasks -> Evaluate Agent inspects execution traces.", 10)
    add_bullet(tf, "Trace-Based Feedback", "Refines the inducement wording whenever the agent skips or rejects the script, boosting ASR by over 16.7% across iterations.", 10)
    add_bullet(tf, "Backend Susceptibility", "GLM-4.7: 97.2%, MiniMax-M2.1: 94.7%, GPT-5-mini: 83.8%, Claude-Sonnet-4.6: 47.0% (most resistant but still compromised).", 10)
    add_bullet(tf, "Frontier Transfer", "Successfully compromised GPT-5.4, GLM-5.1, MiniMax-M2.7, and DeepSeek-V4-flash.", 10)

    # ==========================================
    # SLIDE 8: Theme 1 Synthesis - End-to-End Supply Chain Flow
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8)
    add_header(s8, "Theme 1 Synthesis", "Anatomy of an End-to-End Agent Supply-Chain Compromise", 
               "Tracing the complete multi-stage attack pipeline from registry submission to host execution")
    add_footer(s8, 8)

    # 4 Flow Steps horizontally
    step_w = Inches(2.7)
    step_gap = Inches(0.3)
    
    # Step 1
    s1_card = add_card(s8, Inches(0.8), Inches(1.8), step_w, Inches(3.5))
    tf = s1_card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.15)
    tf.margin_top = Inches(0.15)
    p = tf.paragraphs[0]
    p.text = "Phase 1: Registry Infiltration"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = C_BLUE
    add_bullet(tf, "Action", "Attacker crafts skill with trigger tokens & DoD framing.", 9)
    add_bullet(tf, "Paper", "Saha et al. (2026)", 9)
    add_bullet(tf, "Outcome", "Bypasses registry scanners via context overflow or paraphrasing.", 9)

    # Step 2
    s2_card = add_card(s8, Inches(0.8) + step_w + step_gap, Inches(1.8), step_w, Inches(3.5))
    tf = s2_card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.15)
    tf.margin_top = Inches(0.15)
    p = tf.paragraphs[0]
    p.text = "Phase 2: Discovery & Selection"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = C_AMBER
    add_bullet(tf, "Action", "Agent queries registry for user task; trigger collides in vector space.", 9)
    add_bullet(tf, "Paper", "Saha et al. (2026)", 9)
    add_bullet(tf, "Outcome", "Adversarial skill places in Top-3 (86% win rate); agent selects it in 77.6% of trials.", 9)

    # Step 3
    s3_card = add_card(s8, Inches(0.8) + (step_w + step_gap)*2, Inches(1.8), step_w, Inches(3.5))
    tf = s3_card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.15)
    tf.margin_top = Inches(0.15)
    p = tf.paragraphs[0]
    p.text = "Phase 3: Two-Channel Ingestion"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = C_RED
    add_bullet(tf, "Action", "Agent loads SKILL.md; reads front-loaded setup requirement.", 9)
    add_bullet(tf, "Paper", "Jia et al. (2026)", 9)
    add_bullet(tf, "Outcome", "Agent reasoning plane coerced into running auxiliary helper script (80.7% ASR).", 9)

    # Step 4
    s4_card = add_card(s8, Inches(0.8) + (step_w + step_gap)*3, Inches(1.8), step_w, Inches(3.5))
    tf = s4_card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.15)
    tf.margin_top = Inches(0.15)
    p = tf.paragraphs[0]
    p.text = "Phase 4: Client Tool Hijack"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = C_PRIMARY
    add_bullet(tf, "Action", "Payload executes in client; tool poisoning triggers lateral action.", 9)
    add_bullet(tf, "Paper", "Huang et al. (2026)", 9)
    add_bullet(tf, "Outcome", "Credentials exfiltrated, RCE achieved; UI dialogs bypassed by user fatigue.", 9)

    # Bottom Synthesis Banner
    b_card = add_card(s8, Inches(0.8), Inches(5.5), Inches(11.733), Inches(1.3), bg_color=C_BLUE_LIGHT, border_color=C_BLUE_BORDER)
    tf_b = b_card.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = Inches(0.2)
    tf_b.margin_top = Inches(0.12)
    p = tf_b.paragraphs[0]
    p.text = "Core Takeaway for Agentic Security: The Failure of Fragmented Defenses"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_NAVY_ACCENT
    p2 = tf_b.add_paragraph()
    p2.text = "Soft defenses (prompt filtering, static regex, LLM judges) fail because attackers exploit the semantic gap between documentation and execution. Securing agent systems requires end-to-end provenance: from registry signature verification, through semantic taint tracking in reasoning loops, to deterministic capability tokens at runtime."
    p2.font.size = Pt(10)
    p2.font.color.rgb = C_BODY
    p2.space_before = Pt(3)

    # ==========================================
    # SLIDE 9: Section Divider - Theme 2
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9, C_NAVY_DARK)
    
    t_box9 = s9.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(10.9), Inches(4.0))
    tf9 = t_box9.text_frame
    tf9.word_wrap = True
    
    p = tf9.paragraphs[0]
    p.text = "THEME 2: MULTILINGUAL JAILBREAKING & SAFETY ALIGNMENT"
    p.font.name = FONT_HEAD
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RGBColor(52, 211, 153) # Emerald 400
    
    p2 = tf9.add_paragraph()
    p2.text = "Cross-Lingual Generalization, Resource Gaps, and Multi-Turn Exploitation"
    p2.font.name = FONT_HEAD
    p2.font.size = Pt(28)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(255, 255, 255)
    p2.space_before = Pt(10)
    
    p3 = tf9.add_paragraph()
    p3.text = "A deep examination of two critical studies evaluating how linguistic proficiency, tokenization density, and translation quality dictate whether LLM safety alignment holds or collapses."
    p3.font.name = FONT_BODY
    p3.font.size = Pt(13)
    p3.font.color.rgb = RGBColor(203, 213, 225)
    p3.space_before = Pt(10)

    # 2 paper cards
    c_p1 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(4.5), Inches(5.2), Inches(1.6))
    c_p1.fill.solid()
    c_p1.fill.fore_color.rgb = RGBColor(15, 23, 42)
    c_p1.line.color.rgb = RGBColor(51, 65, 85)
    tf = c_p1.text_frame
    tf.word_wrap = True
    tf.margin_top = Inches(0.15)
    tf.margin_left = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Paper 4: Cross-Lingual Generalization of Jailbreaks & Defenses"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(167, 243, 208)
    p2 = tf.add_paragraph()
    p2.text = "Atil et al. (2025)\nEvaluating 10 languages (High/Med/Low), 6 LLMs, Logic vs. Adversarial Suffixes, and Defense Classifiers on HarmBench & AdvBench."
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = RGBColor(226, 232, 240)

    c_p2 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.5), Inches(5.3), Inches(1.6))
    c_p2.fill.solid()
    c_p2.fill.fore_color.rgb = RGBColor(15, 23, 42)
    c_p2.line.color.rgb = RGBColor(51, 65, 85)
    tf = c_p2.text_frame
    tf.word_wrap = True
    tf.margin_top = Inches(0.15)
    tf.margin_left = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Paper 5: Low-Resource African Language Multi-Turn Jailbreaking"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(167, 243, 208)
    p2 = tf.add_paragraph()
    p2.text = "Marx & Dunaiski (2026)\nEvaluating Afrikaans, Kiswahili, isiZulu, and isiXhosa on 7 commercial LLMs; uncovering the Translation Quality Fallacy via human red-teaming."
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = RGBColor(226, 232, 240)

    # ==========================================
    # SLIDE 10: Paper 4 Deep Dive - Cross-Lingual Generalization (Atil et al.)
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s10)
    add_header(s10, "Paper 4 Deep Dive", "Cross-Lingual Generalization of Jailbreaks and Defenses", 
               "Atil, Passonneau, Morstatter (Penn State & USC) — arXiv:2511.00689 | 10 Languages, 6 LLMs, HarmBench & AdvBench")
    add_footer(s10, 10)

    # Stat boxes
    add_stat_box(s10, Inches(0.8), Inches(1.8), Inches(3.7), Inches(1.15), "10 Languages", "High, Med, Low Tiers", "En, Spa, Ger, Ch, Tr, Ar, Kor, Ben, Tel, Swa", C_NAVY_ACCENT)
    add_stat_box(s10, Inches(4.8), Inches(1.8), Inches(3.7), Inches(1.15), "99.5%", "Peak Adversarial ASR", "Andrius25 suffix on Qwen14b (English)", C_RED)
    add_stat_box(s10, Inches(8.8), Inches(1.8), Inches(3.7), Inches(1.15), ">50% Gap", "Cross-Lingual Variance", "Same model unsafe rates vary by language", C_AMBER)

    # 2 Detail Cards
    c1 = add_card(s10, Inches(0.8), Inches(3.15), Inches(5.7), Inches(3.6))
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "The High vs. Low Resource Paradox"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_PRIMARY
    add_bullet(tf, "Standard Queries", "High-resource languages (En, Ger, Spa) exhibit strong safety alignment (GPT-4o En: 4.0%). Low-resource languages show high baseline unsafe rates (up to 45% on Llama8b).", 10)
    add_bullet(tf, "Adversarial Suffix Attack (Andrius25)", "High-resource languages become hyper-vulnerable (94%–99.5% on open LLMs), whereas low-resource languages resist English-optimized suffixes.", 10)
    add_bullet(tf, "The Root Cause", "Adversarial suffixes rely on dense token probability manipulation. In low-resource languages, fragmented subword tokenization degrades suffix optimization transfer.", 10)
    add_bullet(tf, "Proficiency Paradox", "Linguistic proficiency actually amplifies susceptibility to gradient-based or prompt-optimized adversarial attacks.", 10)

    c2 = add_card(s10, Inches(6.8), Inches(3.15), Inches(5.7), Inches(3.6))
    tf = c2.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Logic Jailbreaks & Defense Robustness"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_PRIMARY
    add_bullet(tf, "Formal Logic Exploits", "Converting queries to logical predicates and translating predicate names achieves up to 80% unsafe responses on Qwen7b and 74% on Llama8b.", 10)
    add_bullet(tf, "Evaluation Methodology", "Used GPT-4o LLM-as-judge without translating back to English; validated by native speakers across all 10 languages (Krippendorff alpha > 0.70).", 10)
    add_bullet(tf, "Self-Guard Defense", "Prompt-based self-verification reduces unsafe rates for some models but exhibits severe instability across non-English languages.", 10)
    add_bullet(tf, "Classifier Filters", "Lightweight response classifiers require combining multilingual embeddings with emotion and NLI features to remain robust across languages.", 10)

    # ==========================================
    # SLIDE 11: Paper 5 Deep Dive - Low-Resource Multi-Turn Jailbreaks (Marx & Dunaiski)
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s11)
    add_header(s11, "Paper 5 Deep Dive", "Multilingual Jailbreaking in Low-Resource African Languages", 
               "Marx & Dunaiski (Stellenbosch Univ.) — arXiv:2605.18239 | Multi-Turn Attacks, Translation Fallacy & Human Red-Teaming")
    add_footer(s11, 11)

    # Stat boxes
    add_stat_box(s11, Inches(0.8), Inches(1.8), Inches(2.7), Inches(1.15), "4 Languages", "African Focus", "Afrikaans, Kiswahili, isiZulu, isiXhosa", C_NAVY_ACCENT)
    add_stat_box(s11, Inches(3.8), Inches(1.8), Inches(2.7), Inches(1.15), "r = 0.92", "BLEU Correlation", "Translation quality dictates jailbreak rate", C_BLUE)
    add_stat_box(s11, Inches(6.8), Inches(1.8), Inches(2.7), Inches(1.15), "+16.0%", "Human Surge", "Overall jump from automated to red-team", C_RED)
    add_stat_box(s11, Inches(9.8), Inches(1.8), Inches(2.7), Inches(1.15), "89.39%", "Peak Red-Team ASR", "Afrikaans human red-teaming rate", C_RED)

    # 2 Detail Cards
    c1 = add_card(s11, Inches(0.8), Inches(3.15), Inches(5.7), Inches(3.6))
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Single-Turn Failure vs. Multi-Turn Potency"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_PRIMARY
    add_bullet(tf, "Single-Turn Demise", "Simply translating harmful prompts into low-resource languages is now largely neutralized by modern safety filters across commercial LLMs.", 10)
    add_bullet(tf, "Multi-Turn Escalation", "Distributing harmful intent across sequential conversation turns achieves 52.7%–83.6% in English, 60.0%–78.2% in Afrikaans, and 41.8%–70.9% in Kiswahili.", 10)
    add_bullet(tf, "Evaluated Models", "Tested 7 commercial LLMs: GPT-4o-mini, GPT-4o, Claude-3.5-Haiku, Gemini-2.0-Flash, Gemini-Flash-Lite, DeepSeek-V3, and Grok-3-mini.", 10)
    add_bullet(tf, "Model Resilience Divide", "Claude-3.5-Haiku demonstrated the strongest guardrails across all languages, while DeepSeek-V3 and GPT-4o-mini were the most vulnerable (>70% ASR).", 10)

    c2 = add_card(s11, Inches(6.8), Inches(3.15), Inches(5.7), Inches(3.6))
    tf = c2.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "The Translation Quality Fallacy Exposed"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_PRIMARY
    add_bullet(tf, "The False Safety Illusion", "Automated tests suggested isiXhosa (45.7%) and isiZulu (49.1%) were 'safer' than English (72.7%).", 10)
    add_bullet(tf, "Root Cause Analysis", "Machine translation produced gibberish or altered semantic meaning (CommonCrawl ratio <0.001%). Translation quality metrics correlated massively with success (BLEU r=0.92, METEOR r=0.91).", 10)
    add_bullet(tf, "Human Red-Teaming Surge", "When native speakers refined prompts, jailbreak rates jumped to 58.0% for isiXhosa (+12.3%), 61.7% for isiZulu (+12.7%), and 89.4% for Afrikaans (+20.0%).", 10)
    add_bullet(tf, "Critical Finding", "Low automated jailbreak rates reflect translation breakdown, NOT robust safety alignment. LLMs remain fundamentally unprotected in low-resource tongues.", 10)

    # ==========================================
    # SLIDE 12: Theme 2 Synthesis - The Multilingual Alignment Landscape
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s12)
    add_header(s12, "Theme 2 Synthesis", "Dynamics of Multilingual Alignment & Benchmark Pitfalls", 
               "Synthesizing findings across Atil et al. (2025) and Marx & Dunaiski (2026)")
    add_footer(s12, 12)

    col_w = Inches(3.7)
    gap = Inches(0.3)
    
    c1 = add_card(s12, Inches(0.8), Inches(1.8), col_w, Inches(4.9))
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Attack Vector Evolution"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_BLUE
    add_bullet(tf, "Single-Turn Obsolete", "Direct multilingual translation is largely blocked by frontier safety classifiers.", 10)
    add_bullet(tf, "Formal Logic Exploitation", "Transforming harmful goals into logic formulas bypasses semantic safety classifiers across both high and medium resource tiers.", 10)
    add_bullet(tf, "Multi-Turn Intent Splitting", "Dispersing harm across benign sub-queries circumvents conversation-level input guardrails.", 10)
    add_bullet(tf, "Human Red-Teaming", "Context-aware native speakers exploit cultural nuances that machine translation tools miss.", 10)

    c2 = add_card(s12, Inches(0.8) + col_w + gap, Inches(1.8), col_w, Inches(4.9))
    tf = c2.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "The Resource Asymmetry"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_RED
    add_bullet(tf, "High-Resource Profile", "Deep safety tuning + High token representation = Resists direct harm, but hyper-vulnerable to token-level adversarial optimization.", 10)
    add_bullet(tf, "Low-Resource Profile", "Shallow safety tuning + Sparse token representation = Vulnerable to standard queries and multi-turn dialogs, but resists English token suffixes.", 10)
    add_bullet(tf, "The Tokenizer Barrier", "Adversarial suffix transfer degrades across languages with non-Latin scripts or divergent byte-pair encodings.", 10)
    add_bullet(tf, "Alignment Inequity", "Safety alignment does not generalize; it remains anchored to dominant training languages.", 10)

    c3 = add_card(s12, Inches(0.8) + (col_w + gap)*2, Inches(1.8), col_w, Inches(4.9))
    tf = c3.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "Benchmark Methodology Warnings"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_AMBER
    add_bullet(tf, "The MT Artifact Trap", "Evaluating low-resource safety using commercial machine translation creates dangerous false-negative safety illusions.", 10)
    add_bullet(tf, "Judge Translation Distortion", "Translating non-English responses back to English for automated LLM judges introduces evaluation noise.", 10)
    add_bullet(tf, "Human Ground Truth", "Direct non-English evaluation with native speakers (as demonstrated in both papers) is essential for credible benchmarking.", 10)
    add_bullet(tf, "Need for Multi-Turn Tests", "Static single-turn benchmarks (AdvBench) are insufficient; dynamic multi-turn suites are required.", 10)

    # ==========================================
    # SLIDE 13: Master Cross-Comparison Matrix (All 5 Papers)
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s13)
    add_header(s13, "Comprehensive Comparative Analysis", "Master Cross-Comparison Matrix across All 5 Papers", 
               "Systematic mapping of threat vectors, target models, benchmarks, and defensive vulnerabilities")
    add_footer(s13, 13)

    # Add Table
    t_shape = s13.shapes.add_table(6, 6, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.9))
    tbl = t_shape.table
    tbl.columns[0].width = Inches(1.6) # Paper & Year
    tbl.columns[1].width = Inches(1.8) # Threat Vector
    tbl.columns[2].width = Inches(2.2) # Target Models
    tbl.columns[3].width = Inches(2.0) # Datasets / Setup
    tbl.columns[4].width = Inches(1.8) # Peak ASR / Metric
    tbl.columns[5].width = Inches(2.333) # Defense Failure Point

    headers = ["Paper & Year", "Threat Vector", "Target Models", "Datasets / Benchmarks", "Peak Impact / ASR", "Primary Defense Failure Point"]
    for col_idx, h_text in enumerate(headers):
        cell = tbl.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_NAVY_DARK
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.name = FONT_HEAD
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    row_data = [
        ("Huang et al.\n(2026)", "MCP Tool Poisoning (Client-Side Metadata)", "Claude-Sonnet-4.5, Gemini 2.5 Pro, Cursor models, Grok-code", "STRIDE/DREAD (50+ threats); 4 attacks across 7 MCP clients", "100% Unsafe in Cursor;\n0% Unsafe in Claude Desktop", "Clients lack static validation; dialog parameter truncation & approval fatigue"),
        ("Saha et al.\n(2026)", "Semantic Supply-Chain (SKILL.md Lifecycle)", "GPT-5, GPT-4.1-mini, Gemma-4-31B, Qwen3-235B, BAAI/OpenAI Embeddings", "100 ClawHub skills (5 domains), 400 variants, ClawHub-style vetting", "86.1% Retrieval Win-Rate;\n77.6% Selection Bias;\n100% Governance Bypass", "Registry truncation windows (10k chars); Definition-of-Done checklists; vector collision"),
        ("Jia et al.\n(2026)", "Two-Channel Automated Injection (SkillJect)", "Claude-Sonnet-4.6, GPT-5-mini, GLM-4.7, MiniMax-M2.1; Frontier LLMs", "100 benign skill packages (6.93 files/pkg), 100 paired task folders", "80.7% ASR on Claude Code;\n80.5% ASR on OpenClaw;\n(Naive baseline: 0.0%)", "Prompt filters inspect instructions, ignoring auxiliary helper scripts and setup commands"),
        ("Atil et al.\n(2025)", "Multilingual Jailbreaks (Logic vs. Suffixes)", "GPT-4o, Sonnet 3.5, Qwen2.5-7B/14B, Llama3.1-8B/70B", "HarmBench (200 queries), AdvBench (520 strings), 10 languages", "99.5% ASR on Qwen14b En;\nUnsafe rate varies >50% by language", "Self-Guard fails cross-lingually; classifiers require complex emotion/NLI fusion"),
        ("Marx & Dunaiski\n(2026)", "Multi-Turn Low-Resource African Language Attacks", "GPT-4o-mini, Claude-3.5-Haiku, DeepSeek-V3, Gemini-2.0, Grok-3", "MultiJail (47 clean), MHJ (55 clean), 4 African languages, Human Red-Teaming", "89.4% ASR (Afrikaans human);\n+16% surge via human red-team", "Automated benchmarks blinded by MT errors; multi-turn intent pacing evades filters")
    ]

    for row_idx, r_data in enumerate(row_data, 1):
        bg_col = C_CARD_BG if row_idx % 2 == 1 else RGBColor(241, 245, 249)
        for col_idx, cell_text in enumerate(r_data):
            cell = tbl.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            p = cell.text_frame.paragraphs[0]
            p.text = cell_text
            p.font.name = FONT_BODY
            p.font.size = Pt(8.5)
            p.font.color.rgb = C_PRIMARY
            if col_idx in [0, 4]:
                p.font.bold = True
                p.alignment = PP_ALIGN.CENTER

    # ==========================================
    # SLIDE 14: Defensive Architecture Gaps & Systemic Solutions
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s14)
    add_header(s14, "Defensive Architecture", "Why Soft Defenses Fail & The Blueprint for Deep Defense", 
               "Transitioning from prompt-level heuristics to deterministic runtime enforcement (CONTEXT.md)")
    add_footer(s14, 14)

    # Left: Why Soft Defenses Fail
    c_left = add_card(s14, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.9))
    tf = c_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.25)
    tf.margin_top = Inches(0.25)
    p = tf.paragraphs[0]
    p.text = "Why Soft & Heuristic Defenses Fail"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_RED
    add_bullet(tf, "Prompt-Level Isolation", "XML tags and delimiters are easily overridden by adaptive phrasing, logic transformations, and multi-turn intent pacing.", 10)
    add_bullet(tf, "LLM-as-a-Judge Vetting", "Vulnerable to context-window truncation (Saha et al.), adversarial jailbreaking, and cross-lingual translation distortion.", 10)
    add_bullet(tf, "Human-in-the-Loop Confirmation", "Neutralized by approval fatigue, complex JSON formatting, and UI parameter truncation (Huang et al.).", 10)
    add_bullet(tf, "Static File Scanners", "Easily evaded by decoupling payloads into helper scripts and using operational euphemisms (Jia et al.).", 10)

    # Right: The Blueprint for Deep Defense
    c_right = add_card(s14, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    tf = c_right.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.25)
    tf.margin_top = Inches(0.25)
    p = tf.paragraphs[0]
    p.text = "The Deep Defensive Blueprint"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_GREEN
    add_bullet(tf, "Policy Enforcement Module (PEM)", "Deterministic gateway placed at the tool execution seam that validates behavioral invariants before running scripts or APIs.", 10)
    add_bullet(tf, "Cross-Artifact Taint Propagation", "Tracking untrusted Data Plane labels across SKILL.md, scratchpads, and downstream tool execution arguments.", 10)
    add_bullet(tf, "Scoped Capability Tokens", "Ephemeral, cryptographically signed permissions granting temporary, least-privilege tool access with strict parameter boundaries.", 10)
    add_bullet(tf, "Architectural Segregation", "Physically separating privileged planning LLMs from unprivileged, untrusted data-processing LLMs (Dual-LLM pattern).", 10)
    add_bullet(tf, "Full-Context Multi-Modal Auditing", "Registry scanning without character truncation, analyzing helper scripts, manifest schemas, and runtime sandboxes.", 10)

    # ==========================================
    # SLIDE 15: Future Research Agenda & Discussion Points for Supervisor
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s15)
    add_header(s15, "Research Horizons", "Proposed Research Directions for Group & Thesis Scope", 
               "Actionable projects bridging agent supply-chain security and cross-lingual safety alignment")
    add_footer(s15, 15)

    col_w = Inches(3.7)
    gap = Inches(0.3)
    
    # Proposal 1
    p1 = add_card(s15, Inches(0.8), Inches(1.8), col_w, Inches(3.8))
    tf = p1.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.18)
    p = tf.paragraphs[0]
    p.text = "Proposal 1: Dynamic Taint Tracking for Agent Skills"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_BLUE
    add_bullet(tf, "Objective", "Build a runtime Policy Enforcement Module for agent frameworks (Claude Code, OpenClaw).", 9.5)
    add_bullet(tf, "Method", "Track taint from untrusted SKILL.md through reasoning scratchpads to intercept unauthorized helper-script execution.", 9.5)
    add_bullet(tf, "Novelty", "First deterministic defense against SkillJect and two-channel decoupled attacks.", 9.5)
    add_bullet(tf, "Target Venue", "IEEE S&P / USENIX Security 2027.", 9.5)

    # Proposal 2
    p2 = add_card(s15, Inches(0.8) + col_w + gap, Inches(1.8), col_w, Inches(3.8))
    tf = p2.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.18)
    p = tf.paragraphs[0]
    p.text = "Proposal 2: Cross-Lingual Agent Jailbreak Benchmark"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_AMBER
    add_bullet(tf, "Objective", "Bridge Theme 1 & 2: Investigate multi-turn low-resource attacks against tool-enabled agents.", 9.5)
    add_bullet(tf, "Method", "Evaluate whether low-resource multilingual multi-turn prompts can coerce agents into executing dangerous MCP tools.", 9.5)
    add_bullet(tf, "Novelty", "Current multilingual benchmarks test text generation; this evaluates tool hijacking and agentic action.", 9.5)
    add_bullet(tf, "Target Venue", "NeurIPS / ACL / EMNLP 2027.", 9.5)

    # Proposal 3
    p3 = add_card(s15, Inches(0.8) + (col_w + gap)*2, Inches(1.8), col_w, Inches(3.8))
    tf = p3.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.18)
    p = tf.paragraphs[0]
    p.text = "Proposal 3: Robust Registry Governance Architecture"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_GREEN
    add_bullet(tf, "Objective", "Design a de-biasing and verification framework for skill registries (ClawHub).", 9.5)
    add_bullet(tf, "Method", "Develop adversarial embedding de-ranking, chunked multi-agent verification, and behavioral sandboxing.", 9.5)
    add_bullet(tf, "Novelty", "Direct countermeasure to Saha et al.'s discovery and governance bypass techniques.", 9.5)
    add_bullet(tf, "Target Venue", "CCS / NDSS 2027.", 9.5)

    # Discussion Box
    d_card = add_card(s15, Inches(0.8), Inches(5.8), Inches(11.733), Inches(1.0), bg_color=C_BLUE_LIGHT, border_color=C_BLUE_BORDER)
    tf_d = d_card.text_frame
    tf_d.word_wrap = True
    tf_d.margin_left = Inches(0.2)
    tf_d.margin_top = Inches(0.1)
    p = tf_d.paragraphs[0]
    p.text = "Key Questions for Supervisor Guidance:"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = C_NAVY_ACCENT
    p2 = tf_d.add_paragraph()
    p2.text = "1. Which venue / conference profile aligns best with our group's current trajectory (Security vs. NLP)?\n2. Should we prioritize deterministic runtime agent defenses (Proposal 1) or empirical cross-lingual agent red-teaming (Proposal 2)?"
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = C_BODY
    p2.space_before = Pt(2)

    # ==========================================
    # SLIDE 16: Conclusion & Open Discussion
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s16)
    add_header(s16, "Conclusion", "Summary of Takeaways & Discussion", 
               "Core insights from the literature synthesis and next steps")
    add_footer(s16, 16)

    c1 = add_card(s16, Inches(0.8), Inches(1.8), Inches(3.7), Inches(3.8))
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "1. Skills are Active Code"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_BLUE
    add_bullet(tf, "Not Passive Text", "SKILL.md and MCP schemas are operational control surfaces shaping retrieval, agent reasoning, and system calls.", 10)
    add_bullet(tf, "Supply-Chain Danger", "Malicious third-party packages can reliably manipulate registries and steer agents into executing local payloads.", 10)

    c2 = add_card(s16, Inches(4.8), Inches(1.8), Inches(3.7), Inches(3.8))
    tf = c2.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "2. Alignment is Asymmetric"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_RED
    add_bullet(tf, "Language Inequity", "Safety alignment does not transfer uniformly across languages. High-resource models succumb to adversarial suffixes.", 10)
    add_bullet(tf, "Translation Blindspot", "Automated benchmarks suffer from machine translation artifacts; human red-teaming exposes severe latent vulnerabilities.", 10)

    c3 = add_card(s16, Inches(8.8), Inches(1.8), Inches(3.7), Inches(3.8))
    tf = c3.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "3. Deep Defense Needed"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_GREEN
    add_bullet(tf, "Soft Defenses Fail", "Prompt-level isolation, basic static scanners, and LLM judges are easily bypassed or context-truncated.", 10)
    add_bullet(tf, "Systemic Enforcement", "We must implement deterministic Policy Enforcement Modules, capability tokens, and dynamic taint tracking.", 10)

    # Discussion Box
    end_box = add_card(s16, Inches(0.8), Inches(5.8), Inches(11.733), Inches(1.0), bg_color=C_NAVY_DARK, border_color=C_NAVY_ACCENT)
    tf_end = end_box.text_frame
    tf_end.word_wrap = True
    tf_end.margin_left = Inches(0.2)
    tf_end.margin_top = Inches(0.18)
    p = tf_end.paragraphs[0]
    p.text = "Thank You! Open for Questions & Advisor Guidance"
    p.font.name = FONT_HEAD
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.alignment = PP_ALIGN.CENTER
    p2 = tf_end.add_paragraph()
    p2.text = "Presentation & Research Notes available in repository workspace."
    p2.font.size = Pt(10)
    p2.font.color.rgb = RGBColor(148, 163, 184)
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(3)

    # Save presentation
    prs.save(output_path)
    print(f"Presentation successfully saved to: {output_path}")

if __name__ == "__main__":
    out_file = "/home/almizan/Other Locations/workspace/research/AI_Agent_Security_and_Multilingual_Jailbreaking_Presentation.pptx"
    build_presentation(out_file)
