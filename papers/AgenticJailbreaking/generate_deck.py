import os
import sys
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

def create_deck(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # --- Color Palette ---
    C_DARK_BG       = RGBColor(10, 17, 40)      # Deep Navy/Midnight (#0A1128)
    C_LIGHT_BG      = RGBColor(248, 250, 252)  # Slate-50 (#F8FAFC)
    C_CARD_BG       = RGBColor(255, 255, 255)  # Pure White
    C_CARD_BORDER   = RGBColor(226, 232, 240)  # Slate-200
    C_NAVY_TEXT     = RGBColor(15, 23, 42)     # Slate-900
    C_SLATE_BODY    = RGBColor(51, 65, 85)     # Slate-700
    C_MUTED_TEXT    = RGBColor(100, 116, 139)  # Slate-500
    C_BLUE_ACCENT   = RGBColor(37, 99, 235)    # Blue-600
    C_RED_ACCENT    = RGBColor(220, 38, 38)    # Red-600 (Vulnerabilities/Attacks)
    C_GREEN_ACCENT  = RGBColor(5, 150, 105)    # Emerald-600 (Defenses/Safety)
    C_PURPLE_ACCENT = RGBColor(124, 58, 237)   # Violet-600
    C_AMBER_ACCENT  = RGBColor(217, 119, 6)    # Amber-600
    C_TAG_BG        = RGBColor(239, 246, 255)  # Blue-50
    C_TAG_TEXT      = RGBColor(29, 78, 216)    # Blue-700

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, tag, title, subtitle):
        # Category Tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.733), Inches(0.3))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag.upper()
        p_tag.font.size = Pt(9.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_BLUE_ACCENT

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.733), Inches(0.55))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = C_NAVY_TEXT

        # Subtitle
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.25), Inches(11.733), Inches(0.35))
        tf_sub = sub_box.text_frame
        tf_sub.word_wrap = True
        tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
        p_sub = tf_sub.paragraphs[0]
        p_sub.text = subtitle
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = C_MUTED_TEXT

    def add_footer(slide, current_slide, total_slides=17):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.3))
        tf = footer_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = f"Agentic Jailbreaking & LLM Agent Security | Literature Review & Research Strategy  •  Slide {current_slide} of {total_slides}"
        p.font.size = Pt(8.5)
        p.font.color.rgb = RGBColor(148, 163, 184)

    def add_card(slide, left, top, width, height, fill_color=C_CARD_BG, border_color=C_CARD_BORDER, border_width=1.0):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
        if border_color:
            shape.line.color.rgb = border_color
            shape.line.width = Pt(border_width)
        else:
            shape.line.fill.background()
        return shape

    # =========================================================================
    # SLIDE 1: Title Slide (Dark Navy)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1, C_DARK_BG)

    # Accent pill
    pill = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.1), Inches(3.2), Inches(0.38))
    pill.fill.solid()
    pill.fill.fore_color.rgb = RGBColor(30, 41, 75)
    pill.line.color.rgb = RGBColor(59, 130, 246)
    pill.line.width = Pt(1)
    tf_pill = pill.text_frame
    tf_pill.margin_top = Inches(0.06)
    p_pill = tf_pill.paragraphs[0]
    p_pill.text = "ACADEMIC LITERATURE REVIEW"
    p_pill.font.size = Pt(10)
    p_pill.font.bold = True
    p_pill.font.color.rgb = RGBColor(147, 197, 253)
    p_pill.alignment = PP_ALIGN.CENTER

    # Main Title
    tb_main = slide1.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.8))
    tf_main = tb_main.text_frame
    tf_main.word_wrap = True
    p_m1 = tf_main.paragraphs[0]
    p_m1.text = "Agentic Jailbreaking & LLM Agent Security"
    p_m1.font.size = Pt(36)
    p_m1.font.bold = True
    p_m1.font.color.rgb = RGBColor(255, 255, 255)

    p_m2 = tf_main.add_paragraph()
    p_m2.text = "A Systematic Analysis Across 8 Foundational Papers (2024–2026): Threat Models, Benchmarks & Defense Paradigms"
    p_m2.font.size = Pt(16)
    p_m2.font.color.rgb = RGBColor(148, 163, 184)
    p_m2.space_before = Pt(8)

    # Three summary highlight cards at the bottom of title slide
    card_w = Inches(3.64)
    card_gap = Inches(0.39)
    card_top = Inches(3.8)
    card_h = Inches(2.5)

    c1 = add_card(slide1, Inches(0.8), card_top, card_w, card_h, fill_color=RGBColor(17, 24, 48), border_color=RGBColor(30, 58, 110))
    tf_c1 = c1.text_frame
    tf_c1.word_wrap = True
    tf_c1.margin_left = tf_c1.margin_right = tf_c1.margin_top = Inches(0.25)
    p = tf_c1.paragraphs[0]
    p.text = "8 FOUNDATIONAL PAPERS"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = RGBColor(96, 165, 250)
    p2 = tf_c1.add_paragraph()
    p2.text = "Covering Top Venues"
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(255, 255, 255)
    p2.space_before = Pt(4)
    p3 = tf_c1.add_paragraph()
    p3.text = "• ToolEmu (ICLR 2024)\n• InjecAgent (ACL 2024)\n• ASB (ICLR 2025)\n• WASP (Meta FAIR 2025)\n• SEAgent & LivePI (2026)\n• VIGIL & AgentDojo (2024/26)"
    p3.font.size = Pt(10)
    p3.font.color.rgb = RGBColor(203, 213, 225)
    p3.space_before = Pt(6)

    c2 = add_card(slide1, Inches(0.8) + card_w + card_gap, card_top, card_w, card_h, fill_color=RGBColor(17, 24, 48), border_color=RGBColor(30, 58, 110))
    tf_c2 = c2.text_frame
    tf_c2.word_wrap = True
    tf_c2.margin_left = tf_c2.margin_right = tf_c2.margin_top = Inches(0.25)
    p = tf_c2.paragraphs[0]
    p.text = "THE NEW ATTACK SURFACE"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = RGBColor(248, 113, 113)
    p2 = tf_c2.add_paragraph()
    p2.text = "Beyond Text Generation"
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(255, 255, 255)
    p2.space_before = Pt(4)
    p3 = tf_c2.add_paragraph()
    p3.text = "• Indirect Prompt Injections (IPI)\n• Multi-step Autonomous Exploitation\n• Memory & RAG Poisoning\n• Multi-Agent Confused Deputy\n• Skill Specification Violations"
    p3.font.size = Pt(10)
    p3.font.color.rgb = RGBColor(203, 213, 225)
    p3.space_before = Pt(6)

    c3 = add_card(slide1, Inches(0.8) + (card_w + card_gap)*2, card_top, card_w, card_h, fill_color=RGBColor(17, 24, 48), border_color=RGBColor(30, 58, 110))
    tf_c3 = c3.text_frame
    tf_c3.word_wrap = True
    tf_c3.margin_left = tf_c3.margin_right = tf_c3.margin_top = Inches(0.25)
    p = tf_c3.paragraphs[0]
    p.text = "DEFENSE PARADIGM SHIFT"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = RGBColor(52, 211, 153)
    p2 = tf_c3.add_paragraph()
    p2.text = "From Prompts to Systems"
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(255, 255, 255)
    p2.space_before = Pt(4)
    p3 = tf_c3.add_paragraph()
    p3.text = "• Brittle prompt filtering bypassed\n• Classifiers hurt normal utility\n• Rise of Mandatory Access Control\n• Deterministic SMT trace verification\n• Blueprint for Lab Research"
    p3.font.size = Pt(10)
    p3.font.color.rgb = RGBColor(203, 213, 225)
    p3.space_before = Pt(6)

    add_footer(slide1, 1)

    # =========================================================================
    # SLIDE 2: Executive Summary & The Paradigm Shift
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2, C_LIGHT_BG)
    add_header(slide2, "EXECUTIVE SUMMARY", "The Fundamental Shift: Chatbot Jailbreaks vs. Agentic Jailbreaks", "Why traditional LLM alignment breaks down when models transition from conversation to autonomous tool execution")

    col_w = Inches(5.65)
    col_gap = Inches(0.43)
    col_h = Inches(5.0)

    # Left Card: Traditional Jailbreaks
    card_left = add_card(slide2, Inches(0.8), Inches(1.75), col_w, col_h)
    tf_l = card_left.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.3)
    
    p = tf_l.paragraphs[0]
    p.text = "TRADITIONAL CHATBOT JAILBREAKING"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_MUTED_TEXT

    p2 = tf_l.add_paragraph()
    p2.text = "Text-In, Text-Out Safety Boundary"
    p2.font.size = Pt(16)
    p2.font.bold = True
    p2.font.color.rgb = C_NAVY_TEXT
    p2.space_before = Pt(4)

    bullets_l = [
        ("Confined Impact", "Failure mode is limited to harmful token generation (hate speech, bomb manuals, harmful advice)."),
        ("Single-Turn Human-in-the-Loop", "Adversary directly converses with the model; human must read, verify, and manually act on output."),
        ("Static Context Boundary", "Model operates purely on user prompts and internal weights without observing changing external state."),
        ("Aligned via RLHF", "Post-training safety tuning (RLHF/DPO) suppresses prohibited text sequences relatively reliably.")
    ]
    for b_title, b_desc in bullets_l:
        p_b = tf_l.add_paragraph()
        p_b.text = f"• {b_title}: {b_desc}"
        p_b.font.size = Pt(11)
        p_b.font.color.rgb = C_SLATE_BODY
        p_b.space_before = Pt(10)

    # Right Card: Agentic Jailbreaks
    card_right = add_card(slide2, Inches(0.8) + col_w + col_gap, Inches(1.75), col_w, col_h, border_color=C_BLUE_ACCENT, border_width=1.5)
    tf_r = card_right.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.3)

    p = tf_r.paragraphs[0]
    p.text = "AGENTIC JAILBREAKING & EXPLOITATION"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_BLUE_ACCENT

    p2 = tf_r.add_paragraph()
    p2.text = "Autonomous Real-World Action & Side Effects"
    p2.font.size = Pt(16)
    p2.font.bold = True
    p2.font.color.rgb = C_NAVY_TEXT
    p2.space_before = Pt(4)

    bullets_r = [
        ("Irreversible Side Effects", "Failure mode is tool execution: database deletion, fund transfer, unauthorized email exfiltration, shell commands."),
        ("Indirect Ingestion (IPI)", "Adversary does not need direct prompt access; instructions hide inside emails, web DOM, group chats, or files."),
        ("No Instruction-Data Separation", "LLMs cannot formally distinguish between developer commands, user queries, and external tool outputs."),
        ("Compounding Multi-Step Chains", "A single injected instruction hijacks autonomous loops, pivoting across APIs and multi-agent systems.")
    ]
    for b_title, b_desc in bullets_r:
        p_b = tf_r.add_paragraph()
        p_b.text = f"• {b_title}: {b_desc}"
        p_b.font.size = Pt(11)
        p_b.font.color.rgb = C_SLATE_BODY
        p_b.space_before = Pt(10)

    add_footer(slide2, 2)

    # =========================================================================
    # SLIDE 3: Threat Taxonomy & Attack Vectors
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3, C_LIGHT_BG)
    add_header(slide3, "THREAT TAXONOMY", "Core Attack Vectors in LLM Agent Architectures", "A structured taxonomy mapping how adversaries exploit each stage of the agent execution lifecycle")

    card_w4 = Inches(2.72)
    card_gap4 = Inches(0.28)
    card_h4 = Inches(5.0)

    vectors = [
        ("DIRECT PROMPT INJECTION (DPI)", "Direct User Manipulation", C_AMBER_ACCENT,
         "The user directly issues deceptive or adversarial prompts to trick the agent into overriding system guardrails or invoking restricted tools.",
         "• Jailbreak templates ('DAN', jailbreaks)\n• Overriding tool parameters\n• Bypassing user-level authorization\n• Confusing system role definitions",
         "Peak ASR: 72.7% (ASB Benchmark)"),
        
        ("INDIRECT PROMPT INJECTION (IPI)", "Poisoned External Content", C_RED_ACCENT,
         "Malicious instructions are placed into third-party environments (web DOM, incoming emails, group chats, docs) read by the agent's tools.",
         "• Data exfiltration via HTTP / Email\n• Group-chat command spoofing\n• Unsafe code retrieval & exec\n• Hidden HTML text & URL injections",
         "Group Chat ASR: 100% (LivePI)"),
        
        ("MEMORY & RAG POISONING", "Persistent State Corruption", C_PURPLE_ACCENT,
         "Attackers corrupt the agent's long-term retrieval memory or plan store, ensuring subsequent clean tasks are hijacked long after the injection.",
         "• RAG vector database poisoning\n• Plan-of-Thought (PoT) backdoors\n• Cross-session persistent infection\n• Latent trigger activations",
         "Backdoor ASR: 84.3% (ASB Benchmark)"),
        
        ("CONFUSED DEPUTY & SKILLS", "Privilege Escalation & Skills", C_BLUE_ACCENT,
         "Exploiting multi-agent interaction or third-party skills to manipulate a privileged agent into exceeding its intended least-privilege boundary.",
         "• Low-privilege agent tricks Admin\n• Third-party skill contract violation\n• Cross-agent execution hijacking\n• Missing trace-level preconditions",
         "Single-Call Miss Rate: ~50% (VIGIL)")
    ]

    for i, (v_title, v_sub, v_color, v_desc, v_points, v_stat) in enumerate(vectors):
        c = add_card(slide3, Inches(0.8) + (card_w4 + card_gap4)*i, Inches(1.75), card_w4, card_h4)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = v_title
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = v_color

        p2 = tf.add_paragraph()
        p2.text = v_sub
        p2.font.size = Pt(12)
        p2.font.bold = True
        p2.font.color.rgb = C_NAVY_TEXT
        p2.space_before = Pt(3)

        p3 = tf.add_paragraph()
        p3.text = v_desc
        p3.font.size = Pt(10)
        p3.font.color.rgb = C_SLATE_BODY
        p3.space_before = Pt(8)

        p4 = tf.add_paragraph()
        p4.text = "Key Attack Modalities:"
        p4.font.size = Pt(10)
        p4.font.bold = True
        p4.font.color.rgb = C_NAVY_TEXT
        p4.space_before = Pt(10)

        p5 = tf.add_paragraph()
        p5.text = v_points
        p5.font.size = Pt(9.5)
        p5.font.color.rgb = C_SLATE_BODY
        p5.space_before = Pt(3)

        # Highlight box at bottom
        p_stat = tf.add_paragraph()
        p_stat.text = v_stat
        p_stat.font.size = Pt(10)
        p_stat.font.bold = True
        p_stat.font.color.rgb = v_color
        p_stat.space_before = Pt(16)

    add_footer(slide3, 3)

    # =========================================================================
    # SLIDE 4: Chronological Evolution & Landscape Map
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4, C_LIGHT_BG)
    add_header(slide4, "LITERATURE TIMELINE (2024–2026)", "The Evolution of Agent Security Research", "Tracking the shift from synthetic tool emulators to dynamic benchmarks, production environments, and formal verification")

    era_w = Inches(3.7)
    era_gap = Inches(0.31)
    era_h = Inches(5.0)

    eras = [
        ("PHASE 1: 2024", "Foundation, Emulation & Initial Benchmarks", C_BLUE_ACCENT,
         [
             ("ToolEmu (ICLR 2024)", "Pioneered LLM-emulated tool execution; revealed that safety system prompts still leave 23.9% failure incidence in high-stakes domains."),
             ("InjecAgent (ACL 2024)", "First formal benchmark for IPI in tool agents (1,054 tests); proved function-calling fine-tuning outperforms ReAct prompting."),
             ("AgentDojo (NeurIPS 2024)", "Dynamic execution environments (97 tasks, 629 tests); demonstrated that prompt injection detectors severely harm benign utility.")
         ]),
        ("PHASE 2: 2025", "Lifecycle Formalization & Real-World Web", C_PURPLE_ACCENT,
         [
             ("Agent Security Bench (ICLR 2025)", "Comprehensive formalization of 4 agent lifecycle stages (prompt, tool, memory); introduced Plan-of-Thought backdoor (84.3% ASR)."),
             ("WASP (Meta FAIR 2025)", "End-to-end evaluation on self-hosted GitLab & Reddit; uncovered 'Security by Incompetence' (86% intermediate ASR vs 16.7% completion).")
         ]),
        ("PHASE 3: 2026", "Production Workflows, MAC & Formal Verification", C_GREEN_ACCENT,
         [
             ("SEAgent (2026)", "SELinux-inspired Mandatory Access Control (MAC); eliminated multi-agent Confused Deputy and privilege escalation (0.0% ASR)."),
             ("LivePI (UPenn 2026)", "Production VM workflows across 7 live surfaces; showed group chats have 100% universal vulnerability across next-gen LLMs."),
             ("VIGIL (2026)", "SMT-based trace verification; proved single-call filters miss ~50% of violations; achieved 92.6% F1 with formal execution traces.")
         ])
    ]

    for i, (e_phase, e_title, e_color, e_papers) in enumerate(eras):
        c = add_card(slide4, Inches(0.8) + (era_w + era_gap)*i, Inches(1.75), era_w, era_h)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = e_phase
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = e_color

        p2 = tf.add_paragraph()
        p2.text = e_title
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = C_NAVY_TEXT
        p2.space_before = Pt(3)

        for p_name, p_desc in e_papers:
            p_n = tf.add_paragraph()
            p_n.text = f"▶ {p_name}"
            p_n.font.size = Pt(11)
            p_n.font.bold = True
            p_n.font.color.rgb = C_NAVY_TEXT
            p_n.space_before = Pt(12)

            p_d = tf.add_paragraph()
            p_d.text = p_desc
            p_d.font.size = Pt(10)
            p_d.font.color.rgb = C_SLATE_BODY
            p_d.space_before = Pt(3)

    add_footer(slide4, 4)

    # Helper for Paper Deep-Dive Slides (2-column layout)
    def render_paper_slide(slide_num, tag, title, venue_year, authors, core_problem, benchmark_setup, key_results, defense_insights, limitations):
        s = prs.slides.add_slide(blank_layout)
        set_slide_background(s, C_LIGHT_BG)
        add_header(s, f"PAPER DEEP-DIVE {slide_num-4} | {venue_year}", title, f"Authors: {authors}")

        col_w = Inches(5.65)
        col_gap = Inches(0.43)
        col_h = Inches(5.0)

        # Left Column: Problem & Benchmark Architecture
        cl = add_card(s, Inches(0.8), Inches(1.75), col_w, col_h)
        tfl = cl.text_frame
        tfl.word_wrap = True
        tfl.margin_left = tfl.margin_right = tfl.margin_top = Inches(0.28)

        p = tfl.paragraphs[0]
        p.text = "CORE PROBLEM & MOTIVATION"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_BLUE_ACCENT

        p2 = tfl.add_paragraph()
        p2.text = core_problem
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = C_SLATE_BODY
        p2.space_before = Pt(6)

        p3 = tfl.add_paragraph()
        p3.text = "BENCHMARK & EXPERIMENTAL SETUP"
        p3.font.size = Pt(11)
        p3.font.bold = True
        p3.font.color.rgb = C_NAVY_TEXT
        p3.space_before = Pt(14)

        for b_item in benchmark_setup:
            p_b = tfl.add_paragraph()
            p_b.text = f"• {b_item}"
            p_b.font.size = Pt(10)
            p_b.font.color.rgb = C_SLATE_BODY
            p_b.space_before = Pt(4)

        # Right Column: Results, Defense & Limitations
        cr = add_card(s, Inches(0.8) + col_w + col_gap, Inches(1.75), col_w, col_h)
        tfr = cr.text_frame
        tfr.word_wrap = True
        tfr.margin_left = tfr.margin_right = tfr.margin_top = Inches(0.28)

        p = tfr.paragraphs[0]
        p.text = "EMPIRICAL PERFORMANCE & FINDINGS"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_RED_ACCENT

        for r_item in key_results:
            p_r = tfr.add_paragraph()
            p_r.text = f"▶ {r_item}"
            p_r.font.size = Pt(10)
            p_r.font.color.rgb = C_SLATE_BODY
            p_r.space_before = Pt(4)

        p_d_head = tfr.add_paragraph()
        p_d_head.text = "DEFENSE TAKEAWAY & INSIGHT"
        p_d_head.font.size = Pt(11)
        p_d_head.font.bold = True
        p_d_head.font.color.rgb = C_GREEN_ACCENT
        p_d_head.space_before = Pt(12)

        p_d = tfr.add_paragraph()
        p_d.text = defense_insights
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = C_SLATE_BODY
        p_d.space_before = Pt(4)

        p_l_head = tfr.add_paragraph()
        p_l_head.text = "LIMITATIONS & OPEN GAPS"
        p_l_head.font.size = Pt(11)
        p_l_head.font.bold = True
        p_l_head.font.color.rgb = C_AMBER_ACCENT
        p_l_head.space_before = Pt(12)

        p_l = tfr.add_paragraph()
        p_l.text = limitations
        p_l.font.size = Pt(10)
        p_l.font.color.rgb = C_SLATE_BODY
        p_l.space_before = Pt(4)

        add_footer(s, slide_num)

    # =========================================================================
    # SLIDE 5: ToolEmu (ICLR 2024)
    # =========================================================================
    render_paper_slide(
        5, "PAPER 1",
        "ToolEmu: Identifying the Risks of LM Agents with an LM-Emulated Sandbox",
        "ICLR 2024", "Yangjun Ruan, Honghua Dong, Andrew Wang, Jimmy Ba, Tatsunori Hashimoto, et al. (Toronto, Stanford)",
        "Evaluating high-stakes, long-tail tool execution risks (e.g. medical, smart home, finance) is prohibitively labor-intensive because implementing custom sandbox environments for hundreds of APIs is unsustainable.",
        [
            "ToolEmu Framework: Uses GPT-4 as an emulator to simulate tool execution, returns, and world state updates.",
            "Automatic Safety Evaluator: GPT-4-based evaluator to identify failures and quantify severity (0-3 scale).",
            "Dataset: 36 high-stakes toolkits across 18 categories with 144 test cases covering 9 risk categories.",
            "Evaluated Agents: GPT-4, Claude-2, ChatGPT-3.5, Vicuna-1.5 (13B/7B)."
        ],
        [
            "Human Validation: 68.8% of identified failures were confirmed as valid real-world agent failures.",
            "Evaluator Reliability: Achieved 75.3% precision and 73.1% recall (Cohen's κ > 0.45, matching human agreement).",
            "Failure Incidence: Standard GPT-4 failed 39.4% of cases; Claude-2: 44.3%; ChatGPT-3.5: 62.0%; Vicuna-13B: 54.6%."
        ],
        "Adding explicit safety requirements into system prompts boosts safety scores and reduces GPT-4 failure rate from 39.4% to 23.9%. However, even the safest agent still causes critical failures in nearly 1 in 4 cases.",
        "Test case curation relied on manual human design (LM generation produced invalid tests); the LM emulator can occasionally overlook physical constraints or hallucinate tool outcomes in complex adversarial scenarios."
    )

    # =========================================================================
    # SLIDE 6: InjecAgent (ACL 2024)
    # =========================================================================
    render_paper_slide(
        6, "PAPER 2",
        "InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLMs",
        "Findings of ACL 2024", "Qiusi Zhan, Zhixiang Liang, Zifan Ying, Daniel Kang (UIUC)",
        "Tool-integrated agents routinely read external content (emails, webpages) where attackers can embed indirect prompt injections (IPI) to hijack tool execution without direct user interaction.",
        [
            "Threat Taxonomy: Categorizes attacks into Direct Harm (file deletion, unauthorized actions) and Data Stealing (exfiltration).",
            "Benchmark Scale: 1,054 test cases covering 17 user tools and 62 attacker tools across Base and Enhanced settings.",
            "Settings: Base setting (pure attacker text) vs Enhanced setting (attacker text augmented with a hacking prompt).",
            "Models Tested: 30 agents across prompted ReAct (GPT-4, Claude-2, LLaMA-2, Mistral, Qwen) and fine-tuned models."
        ],
        [
            "Prompted GPT-4: Suffered 24% ASR in Base setting, nearly doubling to 47% ASR in Enhanced setting.",
            "Prompted LLaMA-2-70B: Highly susceptible, exhibiting >80% ASR across both settings.",
            "Fine-Tuned Function Calling: GPT-4 and GPT-3.5 had drastically lower ASRs: 3.8% and 6.6%, respectively.",
            "Two-Step Exfiltration: Step 2 (transmitting extracted private data) achieved up to 100% success once extracted."
        ],
        "Fine-tuning for tool use (native function calling) provides substantially stronger robustness than ReAct prompting. However, once an agent extracts private data, transmission is almost impossible to stop under prompt defenses.",
        "Relies on a fixed hacking prompt rather than adaptive attacks; external content only contained malicious instructions without realistic interspersed benign text; limited to single-turn, 2-step maximum actions."
    )

    # =========================================================================
    # SLIDE 7: AgentDojo (NeurIPS 2024)
    # =========================================================================
    render_paper_slide(
        7, "PAPER 3",
        "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks & Defenses",
        "NeurIPS 2024 (Datasets & Benchmarks)", "Edoardo Debenedetti, Jie Zhang, Mislav Balunovic, Luca Beurer-Kellner, Florian Tramèr, et al. (ETH Zurich, Invariant Labs)",
        "Static benchmarks fail to capture the evolving nature of prompt injection attacks and defenses. Agents need an extensible, executable benchmark with realistic databases, tasks, and adaptive attacker evaluation.",
        [
            "Environment: 97 realistic agent tasks across 4 core application suites: Workspace, Banking, Slack, and Travel.",
            "Test Suite: 629 security test cases with diverse attacker goals and untrusted tool outputs.",
            "Evaluated Backbones: 10 models including GPT-4o, GPT-4 Turbo, GPT-3.5 Turbo, Claude 3/3.5, Gemini 1.5, Llama 3 70B.",
            "Defenses Tested: Delimiting, Prompt Injection (PI) Detectors, Repeat Prompting, and Tool Filtering/Isolation."
        ],
        [
            "Targeted ASR: GPT-4o was most vulnerable at 47.69%, Claude 3.5 Sonnet at 33.86%, GPT-4 Turbo at 28.62%, Gemini 1.5 Pro at 25.60%.",
            "Untargeted Attacks: Injections successfully derailed models from original tasks in up to 68.36% of cases.",
            "Defense Tradeoffs (GPT-4o): Delimiting (41.65% ASR); Repeat Prompt (27.82% ASR); PI Detector (7.95% ASR, but benign utility crashed from 69.0% to 41.49%)."
        ],
        "Auxiliary PI detectors cause unacceptable benign false positives (severe utility drop). Tool Filtering / Least-Privilege Isolation was the most effective defense (lowered ASR to 6.84% while maintaining 73.13% utility) when tasks only require read access.",
        "Limited to text-based tool interactions (no visual/GUI agents); attacks are largely heuristic; simulated in-memory Python mock environments rather than live real-world external services."
    )

    # =========================================================================
    # SLIDE 8: ASB (ICLR 2025)
    # =========================================================================
    render_paper_slide(
        8, "PAPER 4",
        "Agent Security Bench (ASB): Formalizing Attacks & Defenses in LLM Agents",
        "ICLR 2025", "Hanrong Zhang, Jingyuan Huang, Kai Mei, Hongwei Wang, Yongfeng Zhang, et al. (Zhejiang, Rutgers)",
        "Existing benchmarks evaluate isolated attacks (mostly IPI) without a formal framework covering the entire operational lifecycle of LLM agents, including system prompts, tool selection, and memory retrieval.",
        [
            "Full Lifecycle Formalization: Formalizes attacks across 4 stages: System Prompt, User Prompt, Tool Use, Memory Retrieval.",
            "New Threat Vectors: Direct Prompt Injection (DPI), IPI, Memory Poisoning, and novel Plan-of-Thought (PoT) Backdoors.",
            "Scale: 10 domain scenarios (finance, driving, e-commerce, healthcare), 10 agents, 400+ tools, 27 attack/defense methods.",
            "13 LLM Backbones: Claude-3.5 Sonnet, GPT-4o, GPT-4o-mini, LLaMA-3 (8B/70B), LLaMA-3.1, Gemma-2, Qwen-2."
        ],
        [
            "Lifecycle Vulnerability: Peak average ASR across all models reached 84.30% for PoT Backdoors and 72.68% for DPI.",
            "Frontier Model Vulnerability: GPT-4o had 64.41% average ASR; Claude-3.5 Sonnet had 56.44% ASR (despite 100% PNA).",
            "Disconnect Between LLM Quality & Security: Standalone model leaderboard scores do not correlate with robustness.",
            "Ineffective Defenses: Paraphrasing (56.87% ASR) and Dynamic Prompt Rewriting (44.45% ASR) left models wide open."
        ],
        "More capable models are frequently more susceptible to multi-step attacks because their superior instruction-following makes them obey adversarial payloads more reliably. Prevention-based prompt defenses incur heavy utility penalties.",
        "Evaluated defenses were primarily single-turn prompt rewriting/filtering; simulated benchmark environments without dynamic network interactions; memory poisoning tested primarily on fixed RAG mock databases."
    )

    # =========================================================================
    # SLIDE 9: WASP (Meta FAIR 2025)
    # =========================================================================
    render_paper_slide(
        9, "PAPER 5",
        "WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks",
        "arXiv 2025", "Ivan Evtimov, Arman Zharmagambetov, Chuan Guo, Aaron Grattafiori, Kamalika Chaudhuri (Meta FAIR)",
        "Existing agent tests over-simplify threat models by using synthetic toys or giving attackers full environment control. There is no end-to-end benchmark testing autonomous web agents on live, multi-step web applications.",
        [
            "Self-Hosted Live Platforms: Tested on fully operational, self-hosted web platforms: GitLab and Reddit.",
            "Real Attacker Objectives: High-consequence goals: password changes, account takeover, repo deletion, malicious posting.",
            "Two Evaluation Dimensions: Intermediate Attack Success (ASR-interm) vs End-to-End Goal Completion (ASR-e2e).",
            "Agents Evaluated: GPT-4o, GPT-4o-mini, OpenAI o1, Claude Sonnet 3.5 v2, Claude Sonnet 3.7 Extended Thinking."
        ],
        [
            "Intermediate ASR: Simple human-written injections derailed agents in up to 85.7% (o1), 58.3% (Claude 3.5), and 42.9% (GPT-4o).",
            "End-to-End ASR: Much lower completion rates: 16.7% for OpenAI o1, 2.4%–6.0% for Claude 3.5, and 0.0%–3.6% for GPT-4o.",
            "Reasoning Models: OpenAI o1 was hijacked in 85.7% of cases and achieved the highest end-to-end completion rate (16.7%).",
            "Instruction Hierarchy: OpenAI's instruction hierarchy defense reduced ASR-e2e to 0% on GPT-4o-mini, but utility fell to 27%."
        ],
        "Reveals the 'Security by Incompetence' paradox: agents are easily hijacked away from benign tasks, but current models fail at complex multi-step web navigation. As autonomous reasoning improves, this accidental protection will vanish.",
        "Currently supports only two web platforms (GitLab and Reddit); lacks other critical verticals (travel booking, online banking); small attack prompt diversity; does not cover desktop OS automation."
    )

    # =========================================================================
    # SLIDE 10: SEAgent (2026)
    # =========================================================================
    render_paper_slide(
        10, "PAPER 6",
        "SEAgent: Taming Privilege Escalation in LLM Agents via Mandatory Access Control",
        "arXiv 2026", "Zimo Ji, Daoyuan Wu, Wenyuan Jiang, Pingchuan Ma, Shuai Wang, Yingjiu Li (HKUST, Lingnan, ETH Zurich)",
        "Over-privileged tool use creates critical privilege escalation vulnerabilities—especially in Multi-Agent Systems (MAS)—including the classic Confused Deputy problem where low-privilege agents hijack trusted ones.",
        [
            "Formal Model & Threat Vectors: Vertical/horizontal escalation, Confused Deputy, untrusted 3rd-party agents, RAG poisoning.",
            "SEAgent Framework: SELinux-inspired Mandatory Access Control (MAC) using a System View execution graph and SEMemory.",
            "Hybrid Security Labeling: Combines automated LLM labeling (OpenAI o1) with human verification for Integrity/Sensitivity.",
            "Benchmarks: Evaluated across InjecAgent, AgentDojo, API-Bank (correctness), and AWS Travel Multi-Agent benchmark."
        ],
        [
            "Zero Attack Success Rate: Achieved 0.00% ASR across all benchmarked attacks on both InjecAgent and AgentDojo.",
            "Mitigated Confused Deputy: Successfully blocked untrusted agents from triggering privileged tools (e.g. smart lock).",
            "Utility Preservation: Maintained 67.91%–74.73% correctness on API-Bank with near-zero false positive rate (0%–5.13%).",
            "Vastly Outperformed IsolateGPT: IsolateGPT suffered up to 34% drop in task accuracy and an 18.31% false positive rate."
        ],
        "Deterministic, system-level Mandatory Access Control eliminates privilege escalation paths without relying on probabilistic LLM detectors or prompt guards. Context-aware execution graph tracking preserves normal agent utility.",
        "Requires pre-labeled security attributes (Integrity, Sensitivity, Privacy) for all tools, databases, and agents; security policies must be defined in advance in the Policy DB; dynamic emergent flows may need manual policy maintenance."
    )

    # =========================================================================
    # SLIDE 11: LivePI (UPenn 2026)
    # =========================================================================
    render_paper_slide(
        11, "PAPER 7",
        "LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injection",
        "arXiv 2026", "Lei Zhao, Abhay Bhaskar, Edgar Dobriban (University of Pennsylvania)",
        "Existing IPI evaluations are small, purely simulated, or limited to isolated channels. They fail to benchmark agent risks in production-like workflows with access to real operating systems and external APIs.",
        [
            "Production VM Environment: Evaluates agents on a live Linux VM running OpenClaw with live email, chat, web, files, and crypto wallet.",
            "7 Input Surfaces: Group Chat (WhatsApp, Telegram, Slack), Email, Local Docs, GitHub Repos, Gist, Web.",
            "5 Malicious Goals: Credential exfiltration, security control alteration, unsafe code execution, inbox theft, crypto transfer.",
            "Next-Gen LLMs: Evaluated GPT-5.3-Codex, Claude Opus 4.6, Gemini 3.1 Pro, Kimi K2.5, GLM-5."
        ],
        [
            "Total ASR Across Backbones: Gemini 3.1 Pro (29.6%), GLM-5 (27.8%), GPT-5.3-Codex (27.2%), Kimi (16.6%), Claude Opus 4.6 (10.7%).",
            "Universal Group Chat Vulnerability: Group chat injections achieved 100.0% ASR across all five models.",
            "Surface Disparity: Repo links produced high-severity compromise (50%–100%), while Gist was mostly ineffective (0%–20%).",
            "Two-Layer Defense: Combining prompt filtering and pre-execution tool-call authorization reduced ASR to 0.0% on GPT-5.3-Codex."
        ],
        "Group chats represent a severe architectural flaw: group messages are ingested into model context under 'role: user', tricking the agent into treating attacker text as authoritative instructions. Pre-execution authorization stops attacks with minimal friction (0.11% block rate).",
        "Defended evaluation was conducted only on GPT-5.3-Codex; defense rules were targeted to known attack classes; repository-link surface had a small sample size (n = 4 cases); tested exclusively within OpenClaw runtime."
    )

    # =========================================================================
    # SLIDE 12: VIGIL (2026)
    # =========================================================================
    render_paper_slide(
        12, "PAPER 8",
        "VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills",
        "arXiv 2026", "Ying Li, Yanju Chen, Hongbo Wen, Yu Feng, Yuan Tian, et al. (UCLA, UCSD, UCSB, Riema Labs)",
        "Third-party AI agent skills ship natural-language behavioral contracts (permissions, disclosure limits, preconditions). However, existing runtime monitors use single-call filters that cannot enforce policies spanning multi-action execution traces.",
        [
            "Trace-Grounded SMT Monitoring: Compiles natural-language skill specifications into formal SMT constraints over finite traces.",
            "Contextual Granularity: Tracks temporal ordering, argument constraints, and cross-call value flows rather than isolated calls.",
            "Evaluation Benchmark: SB+SI (152 labeled real executions from SkillsBench & Skill-Inject: 72 violating, 80 benign).",
            "Real-World Audit: Audited 216 executions of shipped skill bundles from NVIDIA, Databricks, Cloudflare, and Trail of Bits."
        ],
        [
            "High Precision & Recall: On SB+SI, VIGIL achieved 95.8% recall, 89.6% precision, and 92.6% F1 (69/72 violations detected, only 8 FPs).",
            "Superiority Over Single-Call Guards: AgentSpec (57.6% F1) and Progent (50.3% F1) missed ~50% of violations.",
            "Outperformed LLM-as-Judge: claude-opus-4-6 judge achieved only 76.8% F1 and missed 24 temporal violations.",
            "Real-World Impact: Discovered 34 confirmed policy violations across deployed skills (one officially acknowledged by NVIDIA)."
        ],
        "Single-call action boundary defenses fundamentally fail because attack violations manifest across historical preconditions and cross-call data flow. Formal SMT trace checking provides deterministic enforcement with sub-200ms overhead.",
        "Requires compiling natural language skill specifications into formal policy representations; subjective semantic properties (e.g. text tone) require external oracle predicates; monitor introduces solver latency for very long execution histories."
    )

    # =========================================================================
    # SLIDE 13: Cross-Paper Comparative Matrix
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide13, C_LIGHT_BG)
    add_header(slide13, "CROSS-PAPER SYNTHESIS", "Master Benchmark & Architectural Comparison Matrix", "Comprehensive comparison across threat vectors, evaluation fidelity, top models evaluated, peak ASR, and optimal defenses")

    # Table layout
    t_left = Inches(0.8)
    t_top = Inches(1.75)
    t_width = Inches(11.733)
    t_height = Inches(4.9)

    rows, cols = 9, 7
    table_shape = slide13.shapes.add_table(rows, cols, t_left, t_top, t_width, t_height)
    table = table_shape.table

    col_widths = [Inches(1.8), Inches(1.1), Inches(1.8), Inches(1.6), Inches(2.0), Inches(1.4), Inches(2.033)]
    for idx, width in enumerate(col_widths):
        table.columns[idx].width = width

    headers = ["Benchmark / Paper", "Venue/Year", "Primary Threat Vectors", "Eval Fidelity", "Key Models Evaluated", "Peak ASR", "Best Defense Paradigm"]
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_DARK_BG
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    data = [
        ("ToolEmu", "ICLR '24", "High-Stakes Tool Failures", "LM Emulated Sandbox", "GPT-4, Claude-2, ChatGPT-3.5", "62.0% (ChatGPT)", "Safety System Prompts"),
        ("InjecAgent", "ACL '24", "IPI (Harm & Exfiltration)", "Synthetic API Mock", "GPT-4, Claude-2, LLaMA-2-70B", "80%+ (LLaMA2)", "Function-Calling Tuning"),
        ("AgentDojo", "NeurIPS '24", "DPI, IPI in Tool Tasks", "Dynamic In-Memory Py", "GPT-4o, Claude 3.5, Gemini 1.5", "47.7% (GPT-4o)", "Tool Filtering / Least-Priv."),
        ("ASB (Agent Sec)", "ICLR '25", "DPI, IPI, Memory, PoT", "10 Simulated Scenarios", "GPT-4o, Claude 3.5, Qwen2-72B", "84.3% (Backdoor)", "Lifecycle Formalization"),
        ("WASP", "FAIR '25", "Web Prompt Injection", "Self-Hosted Web (GitLab)", "OpenAI o1, Claude 3.5/3.7, 4o", "85.7% (Interm. o1)", "Instruction Hierarchy"),
        ("SEAgent", "arXiv '26", "Priv. Escalation, Confused Dep.", "InjecAgent, AgentDojo, AWS", "GPT-3.5-Turbo, OpenAI o1", "39.1% Naive -> 0%", "Mandatory Access Control (MAC)"),
        ("LivePI", "arXiv '26", "IPI in Local Workflows", "Live Linux VM (OpenClaw)", "GPT-5.3-Codex, Claude Opus 4.6", "100% (Group Chat)", "2-Layer Tool Authorization"),
        ("VIGIL", "arXiv '26", "Agent Skill Contract Breaks", "SB+SI, Deployed Skills", "Claude Sonnet 4.6, GPT-4o", "95.8% Rec. Violat.", "SMT Finite-Trace Checking")
    ]

    for i, row in enumerate(data):
        bg_c = RGBColor(255, 255, 255) if i % 2 == 0 else RGBColor(241, 245, 249)
        for j, val in enumerate(row):
            cell = table.cell(i+1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_c
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(8.5)
            p.font.color.rgb = C_NAVY_TEXT
            if j == 0:
                p.font.bold = True
            if j == 5:
                p.font.bold = True
                p.font.color.rgb = C_RED_ACCENT
            if j == 6:
                p.font.color.rgb = C_GREEN_ACCENT
                p.font.bold = True

    add_footer(slide13, 13)

    # =========================================================================
    # SLIDE 14: Model Vulnerability Across Generations
    # =========================================================================
    slide14 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide14, C_LIGHT_BG)
    add_header(slide14, "CROSS-MODEL ANALYSIS", "The Capability-Security Disconnect Across Model Generations", "Why higher reasoning capabilities frequently lead to higher attack compliance and vulnerability")

    cw3 = Inches(3.7)
    cg3 = Inches(0.31)
    ch3 = Inches(5.0)

    # Card 1: The Disconnect
    c1 = add_card(slide14, Inches(0.8), Inches(1.75), cw3, ch3)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = tf1.margin_top = Inches(0.25)
    p = tf1.paragraphs[0]
    p.text = "THE REASONING PARADOX"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_RED_ACCENT
    p2 = tf1.add_paragraph()
    p2.text = "Higher IQ, Higher Susceptibility"
    p2.font.size = Pt(13)
    p2.font.bold = True
    p2.font.color.rgb = C_NAVY_TEXT
    p2.space_before = Pt(3)

    points1 = [
        ("Better Instruction Following", "Frontier models (GPT-4o, Claude 3.5, OpenAI o1) excel at following complex directives, making them more obedient to injected instructions."),
        ("ASB Leaderboard Finding", "ASB proved that standalone LLM quality on leaderboards does NOT predict agent security. GPT-4o showed 64.41% ASR across attacks."),
        ("WASP Reasoning Finding", "In WASP, OpenAI o1 achieved an 85.7% intermediate attack success rate—the highest among all evaluated models.")
    ]
    for b_title, b_desc in points1:
        pb = tf1.add_paragraph()
        pb.text = f"• {b_title}: {b_desc}"
        pb.font.size = Pt(9.5)
        pb.font.color.rgb = C_SLATE_BODY
        pb.space_before = Pt(8)

    # Card 2: Security by Incompetence
    c2 = add_card(slide14, Inches(0.8) + cw3 + cg3, Inches(1.75), cw3, ch3)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = tf2.margin_top = Inches(0.25)
    p = tf2.paragraphs[0]
    p.text = "ACCIDENTAL PROTECTION"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_AMBER_ACCENT
    p2 = tf2.add_paragraph()
    p2.text = "'Security by Incompetence'"
    p2.font.size = Pt(13)
    p2.font.bold = True
    p2.font.color.rgb = C_NAVY_TEXT
    p2.space_before = Pt(3)

    points2 = [
        ("Intermediate vs Full Attack", "WASP demonstrated that while attacks derail agents in 86% of cases, full end-to-end completion is only 0%–16%."),
        ("Failure to Navigate", "Current agents get stuck on UI popups, complex forms, or multi-step logic, inadvertently halting the attacker's multi-step plan."),
        ("The Impending Cliff", "As frontier agents (Claude 3.7, GPT-5.3) master autonomous navigation and error recovery, this accidental barrier will completely dissolve.")
    ]
    for b_title, b_desc in points2:
        pb = tf2.add_paragraph()
        pb.text = f"• {b_title}: {b_desc}"
        pb.font.size = Pt(9.5)
        pb.font.color.rgb = C_SLATE_BODY
        pb.space_before = Pt(8)

    # Card 3: Context & Architecture Flaws
    c3 = add_card(slide14, Inches(0.8) + (cw3 + cg3)*2, Inches(1.75), cw3, ch3)
    tf3 = c3.text_frame
    tf3.word_wrap = True
    tf3.margin_left = tf3.margin_right = tf3.margin_top = Inches(0.25)
    p = tf3.paragraphs[0]
    p.text = "ARCHITECTURAL HOLES"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_BLUE_ACCENT
    p2 = tf3.add_paragraph()
    p2.text = "Context Role Ingestion Bugs"
    p2.font.size = Pt(13)
    p2.font.bold = True
    p2.font.color.rgb = C_NAVY_TEXT
    p2.space_before = Pt(3)

    points3 = [
        ("The Role:User Vulnerability", "LivePI revealed that in group messaging (Slack, Telegram), member messages enter context as 'role: user', causing 100% universal exploitability across all models."),
        ("Fine-Tuning Helps But Isn't Enough", "InjecAgent proved fine-tuned function calling reduces ASR from 24% to 3.8%, but data exfiltration still hits 100% once sensitive data is read."),
        ("Lack of Native Taint Tracking", "Transformer architectures have no hardware-level distinction between control flow and data flow.")
    ]
    for b_title, b_desc in points3:
        pb = tf3.add_paragraph()
        pb.text = f"• {b_title}: {b_desc}"
        pb.font.size = Pt(9.5)
        pb.font.color.rgb = C_SLATE_BODY
        pb.space_before = Pt(8)

    add_footer(slide14, 14)

    # =========================================================================
    # SLIDE 15: The Defense Evolution
    # =========================================================================
    slide15 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide15, C_LIGHT_BG)
    add_header(slide15, "DEFENSE PARADIGM SHIFT", "The Three Waves of LLM Agent Defenses", "Tracing the transition from brittle prompt heuristics to auxiliary ML detectors, and finally deterministic formal system controls")

    col_w3 = Inches(3.7)
    col_gap3 = Inches(0.31)
    col_h3 = Inches(5.0)

    waves = [
        ("WAVE 1: 2023–2024", "Prompt-Level Guidance & Heuristics", C_AMBER_ACCENT,
         "Mechanisms: System prompt safety rules, XML delimiting tags, repeat prompting, input paraphrasing.",
         [
             ("Strengths", "Trivially simple to implement; requires zero changes to agent architecture or tools."),
             ("Flaws", "Brittle and easily bypassed by hacking prompts; ASB showed Paraphrasing still leaves 56.9% ASR."),
             ("Utility Penalty", "Substantially reduces agent instruction-following precision on benign queries.")
         ],
         "Verdict: Inadequate for production agents"),
        
        ("WAVE 2: 2024–2025", "Auxiliary Classifiers & Sandboxing", C_PURPLE_ACCENT,
         "Mechanisms: External PI detectors (Llama-Guard, PromptArmor), Dual-LLM intent planners (CaMeL, IsolateGPT).",
         [
             ("Strengths", "Significantly drops ASR for known injection patterns (AgentDojo PI detector dropped ASR to 7.95%)."),
             ("Flaws", "High False Positive rate; severely harms benign utility (AgentDojo utility crashed from 69% to 41.5%)."),
             ("Vulnerabilities", "Vulnerable to cascading injections where the guard LLM itself is compromised.")
         ],
         "Verdict: Stronger safety, unacceptable friction"),
        
        ("WAVE 3: 2026+", "Deterministic MAC & SMT Verification", C_GREEN_ACCENT,
         "Mechanisms: Mandatory Access Control (SEAgent), System View execution graphs, and trace-level SMT checking (VIGIL).",
         [
             ("Strengths", "Achieves 0.0% ASR; eliminates multi-agent Confused Deputy; VIGIL achieves 92.6% F1 on skills."),
             ("Formal Guarantees", "Evaluates temporal prerequisites and information flow across the full execution trace."),
             ("Utility Preservation", "Maintains benign task success with low friction (0.11% block rate on PinchBench).")
         ],
         "Verdict: The future of secure agent systems")
    ]

    for i, (w_era, w_title, w_color, w_mech, w_items, w_verdict) in enumerate(waves):
        c = add_card(slide15, Inches(0.8) + (col_w3 + col_gap3)*i, Inches(1.75), col_w3, col_h3)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = w_era
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = w_color

        p2 = tf.add_paragraph()
        p2.text = w_title
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = C_NAVY_TEXT
        p2.space_before = Pt(3)

        p3 = tf.add_paragraph()
        p3.text = w_mech
        p3.font.size = Pt(9.5)
        p3.font.italic = True
        p3.font.color.rgb = C_MUTED_TEXT
        p3.space_before = Pt(6)

        for it_title, it_desc in w_items:
            pit = tf.add_paragraph()
            pit.text = f"• {it_title}: {it_desc}"
            pit.font.size = Pt(9.5)
            pit.font.color.rgb = C_SLATE_BODY
            pit.space_before = Pt(8)

        pv = tf.add_paragraph()
        pv.text = f"▶ {w_verdict}"
        pv.font.size = Pt(10.5)
        pv.font.bold = True
        pv.font.color.rgb = w_color
        pv.space_before = Pt(16)

    add_footer(slide15, 15)

    # =========================================================================
    # SLIDE 16: Research Opportunities & Lab Directions
    # =========================================================================
    slide16 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide16, C_LIGHT_BG)
    add_header(slide16, "RESEARCH AGENDA FOR OUR LAB", "Concrete Research Directions & Proposal for Supervisor", "Four high-impact, publishable research directions capitalizing on unresolved gaps in agentic jailbreaking")

    card_w4 = Inches(2.72)
    card_gap4 = Inches(0.28)
    card_h4 = Inches(5.0)

    directions = [
        ("DIRECTION 1", "Automated Multi-Turn Red Teaming", C_RED_ACCENT,
         "Developing autonomous red-teaming agents that generate adaptive, multi-turn prompt injections against modern defense frameworks.",
         "• Current benchmarks use static or single-turn injections.\n• Train an adversarial LLM agent to navigate environments, evade MAC policies, and exploit state.\n• Target: S&P / USENIX Security / CCS.",
         "High Novelty / High Impact"),
        
        ("DIRECTION 2", "Automatic SMT Policy Synthesis", C_BLUE_ACCENT,
         "Automating the compilation of vague human task intents and skill docs into provably sound SMT trace policies.",
         "• VIGIL and SEAgent rely on pre-existing or semi-manual policy rules.\n• Research question: Can an LLM synthesize sound, verifiable formal policies with zero human intervention?\n• Target: CAV / PLDI / ICLR.",
         "Formal Methods & AI Convergence"),
        
        ("DIRECTION 3", "Multimodal Agent Jailbreaking", C_PURPLE_ACCENT,
         "Investigating adversarial visual injections targeting computer-use and vision-language navigation agents.",
         "• WASP and LivePI revealed desktop/web agent flaws, but only tested text injections.\n• Screen-space typographic attacks, visual steganography, and adversarial UI elements.\n• Target: NeurIPS / CVPR / ICML.",
         "Frontier & Fast-Moving"),
        
        ("DIRECTION 4", "Information Flow in MCP Protocols", C_GREEN_ACCENT,
         "Designing provable Non-Interference and Taint Tracking for Model Context Protocol (MCP) ecosystems.",
         "• Anthropic's MCP is rapidly becoming the universal standard for tool use.\n• Integrate dynamic taint tracking into MCP tool servers to mathematically prevent data exfiltration.\n• Target: IEEE S&P / NDSS.",
         "Immediate Industry Utility")
    ]

    for i, (d_tag, d_title, d_color, d_desc, d_points, d_badge) in enumerate(directions):
        c = add_card(slide16, Inches(0.8) + (card_w4 + card_gap4)*i, Inches(1.75), card_w4, card_h4)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = d_tag
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = d_color

        p2 = tf.add_paragraph()
        p2.text = d_title
        p2.font.size = Pt(12)
        p2.font.bold = True
        p2.font.color.rgb = C_NAVY_TEXT
        p2.space_before = Pt(3)

        p3 = tf.add_paragraph()
        p3.text = d_desc
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = C_SLATE_BODY
        p3.space_before = Pt(8)

        p4 = tf.add_paragraph()
        p4.text = "Key Contributions:"
        p4.font.size = Pt(9.5)
        p4.font.bold = True
        p4.font.color.rgb = C_NAVY_TEXT
        p4.space_before = Pt(8)

        p5 = tf.add_paragraph()
        p5.text = d_points
        p5.font.size = Pt(9)
        p5.font.color.rgb = C_SLATE_BODY
        p5.space_before = Pt(3)

        p_badge = tf.add_paragraph()
        p_badge.text = f"★ {d_badge}"
        p_badge.font.size = Pt(9.5)
        p_badge.font.bold = True
        p_badge.font.color.rgb = d_color
        p_badge.space_before = Pt(14)

    add_footer(slide16, 16)

    # =========================================================================
    # SLIDE 17: Conclusion & Strategic Summary (Dark Navy)
    # =========================================================================
    slide17 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide17, C_DARK_BG)

    # Main Title
    tb_end = slide17.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(1.2))
    tf_end = tb_end.text_frame
    tf_end.word_wrap = True
    p_e1 = tf_end.paragraphs[0]
    p_e1.text = "Strategic Conclusion & Key Takeaways"
    p_e1.font.size = Pt(28)
    p_e1.font.bold = True
    p_e1.font.color.rgb = RGBColor(255, 255, 255)

    p_e2 = tf_end.add_paragraph()
    p_e2.text = "Summary points to align with supervisor on our lab's immediate research focus"
    p_e2.font.size = Pt(14)
    p_e2.font.color.rgb = RGBColor(148, 163, 184)
    p_e2.space_before = Pt(4)

    # 4 horizontal takeaway cards
    card_w2 = Inches(5.65)
    card_h2 = Inches(2.3)
    card_gap2_x = Inches(0.43)
    card_gap2_y = Inches(0.3)
    start_y = Inches(2.1)

    concl_items = [
        ("1. Agentic Jailbreaking is Fundamentally Distinct",
         "The transition from conversational text generation to autonomous tool invocation expands the attack surface to include irreversible physical and digital side effects. Prompt safety alignment (RLHF) alone cannot prevent tool misuse.",
         RGBColor(96, 165, 250)),
        ("2. Capability Does Not Guarantee Security",
         "Smarter models (o1, GPT-4o, Claude 3.5) exhibit equal or higher attack compliance due to superior instruction-following. The current low end-to-end attack completion is 'Security by Incompetence' that will vanish.",
         RGBColor(248, 113, 113)),
        ("3. Defenses Must Be Deterministic & System-Level",
         "Prompt filters and ML classifiers are easily bypassed and degrade normal utility. The state-of-the-art has decisively moved toward Mandatory Access Control (SEAgent) and SMT trace verification (VIGIL).",
         RGBColor(52, 211, 153)),
        ("4. Immediate Next Step for Our Research",
         "Recommend selecting either: (A) Automated Multi-Turn Red Teaming against MAC/SMT guards, or (B) Formal Information Flow Tracking for the Model Context Protocol (MCP) as our lab's primary target.",
         RGBColor(251, 191, 36))
    ]

    coords = [
        (Inches(0.8), start_y),
        (Inches(0.8) + card_w2 + card_gap2_x, start_y),
        (Inches(0.8), start_y + card_h2 + card_gap2_y),
        (Inches(0.8) + card_w2 + card_gap2_x, start_y + card_h2 + card_gap2_y)
    ]

    for idx, ((c_title, c_text, c_color), (cx, cy)) in enumerate(zip(concl_items, coords)):
        card = add_card(slide17, cx, cy, card_w2, card_h2, fill_color=RGBColor(17, 24, 48), border_color=RGBColor(30, 58, 110))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = c_title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = c_color

        p2 = tf.add_paragraph()
        p2.text = c_text
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = RGBColor(203, 213, 225)
        p2.space_before = Pt(8)

    add_footer(slide17, 17)

    # Save presentation
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    out_dir = "/home/almizan/Other Locations/workspace/research/papers/AgenticJailbreaking"
    out_file = os.path.join(out_dir, "Agentic_Jailbreaking_Literature_Review.pptx")
    create_deck(out_file)
    # Also save to workspace root for easy user download
    root_file = "/home/almizan/Other Locations/workspace/research/Agentic_Jailbreaking_Literature_Review.pptx"
    create_deck(root_file)
