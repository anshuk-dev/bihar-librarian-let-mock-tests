import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)

from part1_units1_3_data import UNITS_1_3_QUESTIONS
from part1_units4_5_data import UNITS_4_5_QUESTIONS
from part2_gs_data import PART2_QUESTIONS

class NumberedCanvas(canvas.Canvas):
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
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Header on page 2 and later
        if self._pageNumber > 1:
            self.drawString(36, 814, "BIHAR SCHOOL LIBRARIAN ELIGIBILITY TEST (LET / SLET) — MODEL MOCK PAPER 01")
            self.drawRightString(559, 814, "BSEB 150 MCQs BLUEPRINT")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.75)
            self.line(36, 808, 559, 808)

        # Footer on all pages
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(36, 32, 559, 32)
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(36, 20, "Bihar State School Librarian Eligibility Examination (LET) | Authentic Previous-Year Aligned Set")
        self.drawRightString(559, 20, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()


def build_pdf(filename="Bihar_Librarian_LET_Model_Paper_01.pdf"):
    all_questions = UNITS_1_3_QUESTIONS + UNITS_4_5_QUESTIONS + PART2_QUESTIONS
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

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#0F172A'),
        alignment=1 # Center
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1E3A8A'),
        alignment=1 # Center
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155'),
        alignment=1
    )

    inst_head = ParagraphStyle(
        'InstHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#0F172A')
    )

    inst_body = ParagraphStyle(
        'InstBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor('#334155')
    )

    part_header_style = ParagraphStyle(
        'PartHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=1
    )

    unit_header_style = ParagraphStyle(
        'UnitHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#1E3A8A')
    )

    q_num_style = ParagraphStyle(
        'QNum',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1E293B')
    )

    q_text_style = ParagraphStyle(
        'QText',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#0F172A')
    )

    opt_style = ParagraphStyle(
        'OptionText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1E293B')
    )

    ans_table_style = ParagraphStyle(
        'AnsTableCell',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        alignment=1
    )

    ans_q_style = ParagraphStyle(
        'AnsQStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#475569'),
        alignment=1
    )

    exp_head_style = ParagraphStyle(
        'ExpHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1E3A8A')
    )

    exp_body_style = ParagraphStyle(
        'ExpBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#334155')
    )

    story = []

    # ------------------ COVER / HEADER ------------------
    story.append(Paragraph("BIHAR SCHOOL EXAMINATION BOARD (BSEB), PATNA", subtitle_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("BIHAR SCHOOL LIBRARIAN ELIGIBILITY TEST (LET / SLET)", title_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>FULL-LENGTH MODEL MOCK TEST PAPER — 01</b>", subtitle_style))
    story.append(Spacer(1, 6))

    # Meta banner table
    meta_data = [
        [
            Paragraph("<b>Total Questions:</b> 150 MCQs", meta_style),
            Paragraph("<b>Total Marks:</b> 150 Marks", meta_style),
            Paragraph("<b>Time Allowed:</b> 2 Hours 30 Minutes", meta_style),
            Paragraph("<b>Negative Marking:</b> None", meta_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[130, 130, 135, 125])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))

    # Instructions Box
    instructions = [
        [Paragraph("<b>IMPORTANT INSTRUCTIONS FOR CANDIDATES:</b>", inst_head)],
        [Paragraph(
            "1. This model question booklet contains <b>150 objective-type Multiple Choice Questions (MCQs)</b> divided into two parts:<br/>"
            "   &bull; <b>Part 1 (Q1 to Q100):</b> Library and Information Science (Core Specialized Domain - 100 Marks)<br/>"
            "   &bull; <b>Part 2 (Q101 to Q150):</b> General Knowledge, Bihar Special GK, General Studies, Science & Mental Ability (50 Marks)<br/>"
            "2. All questions carry equal marks (1 mark each). There is <b>no negative marking</b> for incorrect responses.<br/>"
            "3. Choose only one correct answer from the four options (A, B, C, D) provided with each question.<br/>"
            "4. A complete <b>Official Answer Key Matrix</b> and <b>Detailed Explanations & Notes</b> are provided at the end of this booklet.",
            inst_body
        )]
    ]
    inst_table = Table(instructions, colWidths=[520])
    inst_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#BFDBFE')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(inst_table)
    story.append(Spacer(1, 10))

    # ------------------ QUESTIONS SECTION ------------------
    current_part = None
    current_unit = None

    for q in all_questions:
        # Check for Part banner
        if q['section'] != current_part:
            current_part = q['section']
            part_bg = colors.HexColor('#1E3A8A') if "Part 1" in current_part else colors.HexColor('#0D9488')
            banner = Table([[Paragraph(f"<b>{current_part.upper()}</b>", part_header_style)]], colWidths=[520])
            banner.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), part_bg),
                ('TOPPADDING', (0,0), (-1,-1), 5),
                ('BOTTOMPADDING', (0,0), (-1,-1), 5),
                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ]))
            story.append(Spacer(1, 6))
            story.append(banner)
            story.append(Spacer(1, 6))

        # Check for Unit banner
        if q['unit'] != current_unit:
            current_unit = q['unit']
            unit_banner = Table([[Paragraph(f"&para; <b>{current_unit}</b>", unit_header_style)]], colWidths=[520])
            unit_banner.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
                ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('BOTTOMPADDING', (0,0), (-1,-1), 3),
                ('LEFTPADDING', (0,0), (-1,-1), 8),
            ]))
            story.append(Spacer(1, 4))
            story.append(unit_banner)
            story.append(Spacer(1, 5))

        # Format Question Item
        q_num_text = f"Q{q['id']}."
        q_text = q['question']
        
        # Options formatted 2x2 grid
        opt_a = Paragraph(f"<b>(A)</b> {q['options'][0][3:]}", opt_style)
        opt_b = Paragraph(f"<b>(B)</b> {q['options'][1][3:]}", opt_style)
        opt_c = Paragraph(f"<b>(C)</b> {q['options'][2][3:]}", opt_style)
        opt_d = Paragraph(f"<b>(D)</b> {q['options'][3][3:]}", opt_style)

        q_flow = [
            Table([
                [Paragraph(q_num_text, q_num_style), Paragraph(q_text, q_text_style)]
            ], colWidths=[32, 488], style=[
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
                ('LEFTPADDING', (0,0), (-1,-1), 12),
                ('RIGHTPADDING', (0,0), (-1,-1), 4),
                ('TOPPADDING', (0,0), (-1,-1), 1),
                ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ]),
            Spacer(1, 4),
            HRFlowable(width="100%", thickness=0.3, color=colors.HexColor('#E2E8F0'), spaceBefore=2, spaceAfter=4)
        ]

        story.append(KeepTogether(q_flow))

    # ------------------ OFFICIAL ANSWER KEY MATRIX ------------------
    story.append(PageBreak())
    ans_banner = Table([[Paragraph("<b>OFFICIAL ANSWER KEY MATRIX (QUESTIONS 1 TO 150)</b>", part_header_style)]], colWidths=[520])
    ans_banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1E3A8A')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(ans_banner)
    story.append(Spacer(1, 10))

    # Build 10 columns grid for answer key
    # 15 rows, each row has: Q#, Ans, Q#, Ans, Q#, Ans, Q#, Ans, Q#, Ans
    # Actually let's do 10 columns: Q1-15, Q16-30, ...
    # Standard format: Table with 15 columns or 10 columns (5 blocks of Q and Ans)
    # Block 1: Q1..30, Block 2: Q31..60, Block 3: Q61..90, Block 4: Q91..120, Block 5: Q121..150
    # Let's make a 10-column table (5 groups of [Q, Ans]) with 30 rows.
    matrix_rows = []
    # Header row
    hdr = []
    for _ in range(5):
        hdr.extend([Paragraph("<b>Q.No</b>", ans_q_style), Paragraph("<b>Ans</b>", ans_table_style)])
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

    col_w = [28, 24] * 5  # Total width = 52 * 5 = 260? Wait: 520 / 10 = 52 pt each (e.g. 28 + 24 = 52)
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
    story.append(Spacer(1, 15))

    # ------------------ DETAILED EXPLANATIONS & NOTES ------------------
    story.append(PageBreak())
    exp_banner = Table([[Paragraph("<b>COMPREHENSIVE SOLUTIONS, EXPLANATIONS & CONCEPT NOTES</b>", part_header_style)]], colWidths=[520])
    exp_banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F766E')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(exp_banner)
    story.append(Spacer(1, 8))

    current_exp_part = None

    for q in all_questions:
        if q['section'] != current_exp_part:
            current_exp_part = q['section']
            sub_banner = Table([[Paragraph(f"<b>{current_exp_part.upper()} — DETAILED SOLUTIONS</b>", unit_header_style)]], colWidths=[520])
            sub_banner.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
                ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#94A3B8')),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('BOTTOMPADDING', (0,0), (-1,-1), 3),
                ('LEFTPADDING', (0,0), (-1,-1), 8),
            ]))
            story.append(Spacer(1, 6))
            story.append(sub_banner)
            story.append(Spacer(1, 6))

        # Explanation item
        opt_idx = ord(q['answer']) - ord('A')
        chosen_opt_str = q['options'][opt_idx] if 0 <= opt_idx < len(q['options']) else ""

        exp_box = [
            Table([
                [
                    Paragraph(f"<b>Question {q['id']} [Answer: {q['answer']}]</b> — <i>{chosen_opt_str}</i>", exp_head_style)
                ],
                [
                    Paragraph(f"<b>Explanation:</b> {q['explanation']}", exp_body_style)
                ]
            ], colWidths=[520], style=[
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FAFAFA')),
                ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
                ('TOPPADDING', (0,0), (-1,-1), 4),
                ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                ('LEFTPADDING', (0,0), (-1,-1), 8),
                ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ]),
            Spacer(1, 4)
        ]
        story.append(KeepTogether(exp_box))

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF built successfully: {filename}")

if __name__ == '__main__':
    build_pdf()
