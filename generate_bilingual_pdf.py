# -*- coding: utf-8 -*-
import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)

from bilingual_part1_u1 import BILINGUAL_QUESTIONS
from bilingual_part1_u2_u3 import BILINGUAL_U2_U3
from bilingual_part1_u4_u5 import BILINGUAL_U4_U5
from bilingual_part2_gs import BILINGUAL_PART2_GS

# Register Unicode font for Hindi & English
FONT_NAME = 'ArialUnicode'
pdfmetrics.registerFont(TTFont(FONT_NAME, '/Library/Fonts/Arial Unicode.ttf'))

class NumberedBilingualCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont(FONT_NAME, 8)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Header (page 2 onwards)
        if self._pageNumber > 1:
            self.drawString(36, 814, "बिहार विद्यालय पुस्तकालय पात्रता परीक्षा (LET) — द्विभाषी मॉडल पेपर 01")
            self.drawRightString(559, 814, "BSEB 150 MCQs BILINGUAL SET")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.75)
            self.line(36, 808, 559, 808)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(36, 32, 559, 32)
        self.setFont(FONT_NAME, 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(36, 20, "Bihar State Librarian Eligibility Test (LET/SLET) | English & Hindi Bilingual Authentic Paper")
        self.drawRightString(559, 20, f"Page / पृष्ठ {self._pageNumber} of {page_count}")
        self.restoreState()


def build_bilingual_pdf(filename="Bihar_Librarian_Bilingual_Mock_01.pdf"):
    all_questions = BILINGUAL_QUESTIONS + BILINGUAL_U2_U3 + BILINGUAL_U4_U5 + BILINGUAL_PART2_GS
    assert len(all_questions) == 150

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=44,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()

    # Bilingual Paragraph Styles using ArialUnicode
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#1E3A8A'),
        alignment=1
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#334155'),
        alignment=1
    )

    inst_head = ParagraphStyle(
        'InstHead',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#0F172A')
    )

    inst_body = ParagraphStyle(
        'InstBody',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=7.5,
        leading=10.5,
        textColor=colors.HexColor('#334155')
    )

    part_header_style = ParagraphStyle(
        'PartHeader',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=1
    )

    unit_header_style = ParagraphStyle(
        'UnitHeader',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1E3A8A')
    )

    q_num_style = ParagraphStyle(
        'QNum',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1E293B')
    )

    q_text_style = ParagraphStyle(
        'QText',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#0F172A')
    )

    opt_style = ParagraphStyle(
        'OptionText',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#1E293B')
    )

    ans_table_style = ParagraphStyle(
        'AnsTableCell',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=7.5,
        leading=9.5,
        alignment=1
    )

    ans_q_style = ParagraphStyle(
        'AnsQStyle',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#475569'),
        alignment=1
    )

    exp_head_style = ParagraphStyle(
        'ExpHead',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1E3A8A')
    )

    exp_body_style = ParagraphStyle(
        'ExpBody',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=7.5,
        leading=10.5,
        textColor=colors.HexColor('#334155')
    )

    story = []

    # ------------------ COVER / HEADER ------------------
    story.append(Paragraph("<b>बिहार विद्यालय परीक्षा समिति, पटना / BIHAR SCHOOL EXAMINATION BOARD (BSEB)</b>", subtitle_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>बिहार विद्यालय पुस्तकालय पात्रता परीक्षा (LET / SLET)</b>", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>BIHAR SCHOOL LIBRARIAN ELIGIBILITY TEST — MODEL MOCK PAPER 01</b>", subtitle_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>(द्विभाषी प्रारूप: हिंदी एवं अंग्रेजी / Bilingual Format: Hindi & English)</b>", subtitle_style))
    story.append(Spacer(1, 5))

    # Meta banner table
    meta_data = [
        [
            Paragraph("<b>कुल प्रश्न / Total Qs:</b> 150 MCQs", meta_style),
            Paragraph("<b>पूर्णांक / Max Marks:</b> 150", meta_style),
            Paragraph("<b>समय / Duration:</b> 2:30 Hrs (150 Min)", meta_style),
            Paragraph("<b>ऋणात्मक अंक / Neg Marking:</b> शून्य (None)", meta_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[130, 130, 135, 125])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 6))

    # Instructions Box
    instructions = [
        [Paragraph("<b>परीक्षार्थियों के लिए महत्वपूर्ण निर्देश / IMPORTANT INSTRUCTIONS FOR CANDIDATES:</b>", inst_head)],
        [Paragraph(
            "1. इस मॉडल प्रश्न-पुस्तिका में <b>150 वस्तुनिष्ठ बहुविकल्पीय प्रश्न (MCQs)</b> हैं। / This booklet contains 150 MCQs.<br/>"
            "   &bull; <b>भाग 1 (प्रश्न 1 से 100):</b> पुस्तकालय एवं सूचना विज्ञान (मूल विषय - 100 अंक) / Part 1: Library & Info Science (100 Marks)<br/>"
            "   &bull; <b>भाग 2 (प्रश्न 101 से 150):</b> सामान्य ज्ञान, बिहार विशेष, सामान्य अध्ययन एवं तार्किक क्षमता (50 अंक) / Part 2: GK & GS (50 Marks)<br/>"
            "2. प्रत्येक प्रश्न 1 अंक का है। गलत उत्तर के लिए कोई ऋणात्मक अंक (Negative Marking) नहीं काटा जाएगा।<br/>"
            "3. प्रश्न-पत्र के अंत में त्वरित स्व-मूल्यांकन हेतु <b>उत्तर कुंजी (Answer Key Matrix)</b> एवं <b>विस्तृत व्याख्यात्मक समाधान</b> दिए गए हैं।",
            inst_body
        )]
    ]
    inst_table = Table(instructions, colWidths=[520])
    inst_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#BFDBFE')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(inst_table)
    story.append(Spacer(1, 8))

    # ------------------ QUESTIONS SECTION ------------------
    current_part = None
    current_unit = None

    for q in all_questions:
        # Part banner
        if q['section_en'] != current_part:
            current_part = q['section_en']
            part_bg = colors.HexColor('#1E3A8A') if "Part 1" in current_part else colors.HexColor('#0D9488')
            banner = Table([[Paragraph(f"<b>{q['section_hi'].upper()} / {q['section_en'].upper()}</b>", part_header_style)]], colWidths=[520])
            banner.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), part_bg),
                ('TOPPADDING', (0,0), (-1,-1), 4),
                ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ]))
            story.append(Spacer(1, 5))
            story.append(banner)
            story.append(Spacer(1, 5))

        # Unit banner
        if q['unit_en'] != current_unit:
            current_unit = q['unit_en']
            unit_banner = Table([[Paragraph(f"&para; <b>{q['unit_hi']} / {q['unit_en']}</b>", unit_header_style)]], colWidths=[520])
            unit_banner.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
                ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
                ('TOPPADDING', (0,0), (-1,-1), 2.5),
                ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
                ('LEFTPADDING', (0,0), (-1,-1), 8),
            ]))
            story.append(Spacer(1, 4))
            story.append(unit_banner)
            story.append(Spacer(1, 4))

        # Format Question Item (Bilingual: English + Hindi)
        q_num_text = f"<b>Q{q['id']}.</b>"
        bilingual_q_text = f"<b>{q['q_en']}</b><br/><font color='#1E3A8A'><b>{q['q_hi']}</b></font>"

        # Options formatted bilingual
        def format_opt(label, opt_en, opt_hi):
            return Paragraph(f"<b>({label})</b> {opt_en} <br/>&nbsp;&nbsp;&nbsp;&nbsp;<font color='#334155'><i>{opt_hi}</i></font>", opt_style)

        opt_a = format_opt("A", q['options_en'][0], q['options_hi'][0])
        opt_b = format_opt("B", q['options_en'][1], q['options_hi'][1])
        opt_c = format_opt("C", q['options_en'][2], q['options_hi'][2])
        opt_d = format_opt("D", q['options_en'][3], q['options_hi'][3])

        q_flow = [
            Table([
                [Paragraph(q_num_text, q_num_style), Paragraph(bilingual_q_text, q_text_style)]
            ], colWidths=[30, 490], style=[
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('LEFTPADDING', (0,0), (-1,-1), 0),
                ('RIGHTPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 1),
                ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ]),
            Spacer(1, 2),
            Table([
                [opt_a, opt_b],
                [opt_c, opt_d]
            ], colWidths=[260, 260], style=[
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('LEFTPADDING', (0,0), (-1,-1), 10),
                ('RIGHTPADDING', (0,0), (-1,-1), 4),
                ('TOPPADDING', (0,0), (-1,-1), 1),
                ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ]),
            Spacer(1, 3),
            HRFlowable(width="100%", thickness=0.3, color=colors.HexColor('#E2E8F0'), spaceBefore=2, spaceAfter=3)
        ]

        story.append(KeepTogether(q_flow))

    # ------------------ OFFICIAL ANSWER KEY MATRIX ------------------
    story.append(PageBreak())
    ans_banner = Table([[Paragraph("<b>उत्तर कुंजी सारणी (प्रश्न 1 से 150) / OFFICIAL ANSWER KEY MATRIX (Q1 TO Q150)</b>", part_header_style)]], colWidths=[520])
    ans_banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1E3A8A')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(ans_banner)
    story.append(Spacer(1, 8))

    # 10 columns grid for answer key
    matrix_rows = []
    hdr = []
    for _ in range(5):
        hdr.extend([Paragraph("<b>प्र./Q</b>", ans_q_style), Paragraph("<b>उत्तर/Ans</b>", ans_table_style)])
    matrix_rows.append(hdr)

    answers_dict = {q['id']: q['answer'] for q in all_questions}

    for r in range(30):
        row_cells = []
        for col_block in range(5):
            q_id = r + 1 + (col_block * 30)
            if q_id <= 150:
                row_cells.append(Paragraph(f"{q_id}", ans_q_style))
                row_cells.append(Paragraph(f"<b>{answers_dict[q_id]}</b>", ans_table_style))
            else:
                row_cells.append(Paragraph("", ans_q_style))
                row_cells.append(Paragraph("", ans_table_style))
        matrix_rows.append(row_cells)

    col_w = [28, 24] * 5
    ans_table = Table(matrix_rows, colWidths=col_w)
    ans_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E2E8F0')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 1),
        ('RIGHTPADDING', (0,0), (-1,-1), 1),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F8FAFC')])
    ]))
    story.append(ans_table)
    story.append(Spacer(1, 12))

    # ------------------ DETAILED BILINGUAL EXPLANATIONS ------------------
    story.append(PageBreak())
    exp_banner = Table([[Paragraph("<b>विस्तृत व्याख्यात्मक समाधान एवं अवधारणाएं / COMPREHENSIVE BILINGUAL SOLUTIONS & NOTES</b>", part_header_style)]], colWidths=[520])
    exp_banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F766E')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(exp_banner)
    story.append(Spacer(1, 6))

    current_exp_part = None

    for q in all_questions:
        if q['section_en'] != current_exp_part:
            current_exp_part = q['section_en']
            sub_banner = Table([[Paragraph(f"<b>{q['section_hi'].upper()} / {q['section_en'].upper()} — SOLUTIONS</b>", unit_header_style)]], colWidths=[520])
            sub_banner.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
                ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#94A3B8')),
                ('TOPPADDING', (0,0), (-1,-1), 2.5),
                ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
                ('LEFTPADDING', (0,0), (-1,-1), 8),
            ]))
            story.append(Spacer(1, 5))
            story.append(sub_banner)
            story.append(Spacer(1, 5))

        opt_idx = ord(q['answer']) - ord('A')
        chosen_en = q['options_en'][opt_idx]
        chosen_hi = q['options_hi'][opt_idx]

        exp_box = [
            Table([
                [
                    Paragraph(f"<b>प्रश्न/Q. {q['id']} [सही उत्तर / Correct Ans: {q['answer']}]</b> — <i>{chosen_en} ({chosen_hi})</i>", exp_head_style)
                ],
                [
                    Paragraph(f"<b>English Explanation:</b> {q['exp_en']}<br/><font color='#047857'><b>हिंदी व्याख्या:</b></font> {q['exp_hi']}", exp_body_style)
                ]
            ], colWidths=[520], style=[
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FAFAFA')),
                ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('BOTTOMPADDING', (0,0), (-1,-1), 3),
                ('LEFTPADDING', (0,0), (-1,-1), 8),
                ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ]),
            Spacer(1, 3.5)
        ]
        story.append(KeepTogether(exp_box))

    # Build document
    doc.build(story, canvasmaker=NumberedBilingualCanvas)
    print(f"Bilingual PDF built successfully: {filename}")

if __name__ == '__main__':
    build_bilingual_pdf()
