import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto('https://www.amazon.fr/Lepro-Dimmable-Puissant-R%C3%A9glable-Anti-%C3%89blouissement/dp/B095R8KFN3/?_encoding=UTF8&pd_rd_w=kBpcM&content-id=amzn1.sym.678de850-ec61-45a5-ac60-3d5045978e5b%3Aamzn1.symc.9b8fba90-e74e-4690-b98f-edc36fe735a6&pf_rd_p=678de850-ec61-45a5-ac60-3d5045978e5b&pf_rd_r=Q4JK90TKZKXNNQC37GC7&pd_rd_wg=klq0l&pd_rd_r=889d0cf8-3f95-41a8-bea1-a26a5e7bdbbe&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d&th=1')

    expect(page).to_have_title(re.compile('Lepro Lampe de Bureau LED 15W avec Port USB Lampes Bureau Dimmable 96LEDs 655LM, Puissant, Pied Réglable, Moderne, Contrôle Tactile, Anti-Éblouissement Pour Lecture Travail Manucure Couture - Blanc : Amazon.fr: Luminaires et Éclairage'))

def test_get_started_link(page: Page):
    page.goto('https://playwright.dev/')

    page.get_by_role('link', name='Get started').click()

    expect(page.get_by_role('heading', name='Installation')).to_be_visible()