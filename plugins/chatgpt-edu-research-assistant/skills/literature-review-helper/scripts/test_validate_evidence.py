"""Synthetic offline regression tests. No scholarly or workspace validation is implied."""
import copy
import unittest
from validate_evidence import validate

def fixture():
    return {
      'manifest':{'skill_version':'2.0.1','search_date':'2026-09-10','question':'Synthetic test question','minimum_core':1,'required_indexes':[],'quotes_required':'all_core','reported_core':1},
      'records':[{'id':'R1','title':'Synthetic test report','year':2025,'doi':None,'status':'core','access':'full_text','identity_verified':True,'source_url':'https://example.org/report','bibliography':'Synthetic fixture; not a real publication.','relevance':'Direct test fixture','design':'Synthetic comparison','findings':[{'text':'The fixture reports no difference.','locator':'Results, p. 2','basis':'author_report'}],'limitations':[{'text':'Not research evidence.','basis':'reviewer_inference'}],'integrity':{'status':'no_notice_found','checked_on':'2026-09-10','source':'https://example.org/report'},'index_evidence':[],'metrics':[],'quotes':[{'text':'No difference was found.','source_text':'No difference was found. Further tests are needed.','source_url':'https://example.org/report','version':'Synthetic final','citation':'Synthetic (2025, p. 2)','verified':True,'locator':{'printed_page':'2','pdf_page':2}}]}],
      'claims':[{'id':'C1','text':'Synthetic claim.','support_ids':['R1'],'counter_ids':[]}],
      'searches':[{'id':'Q1','provider':'Synthetic fixture','query':'test only','date':'2026-09-10','status':'user_export'}]}

class Checks(unittest.TestCase):
    def test_no_doi_source_is_valid(self):self.assertTrue(validate(fixture())['ok'])
    def test_shortfall_not_padded_by_supplement(self):
        d=fixture();d['manifest']['minimum_core']=2
        r=copy.deepcopy(d['records'][0]);r.update(id='R2',status='supplementary');d['records'].append(r)
        self.assertIn('Core shortfall',str(validate(d)['errors']))
    def test_falsely_reported_count(self):
        d=fixture();d['manifest']['reported_core']=50;self.assertFalse(validate(d)['ok'])
    def test_duplicate_doi_normalizes(self):
        d=fixture();d['records'][0]['doi']='https://doi.org/10.1234/ABC'
        r=copy.deepcopy(d['records'][0]);r.update(id='R2',doi='doi:10.1234/abc');d['records'].append(r);d['manifest']['reported_core']=2
        self.assertIn('duplicate DOI',str(validate(d)['errors']))
    def test_quote_mismatch(self):
        d=fixture();d['records'][0]['quotes'][0]['text']='A large difference was found.';self.assertFalse(validate(d)['ok'])
    def test_missing_locator(self):
        d=fixture();d['records'][0]['quotes'][0]['locator']={};self.assertFalse(validate(d)['ok'])
    def test_section_locator_without_fake_page(self):
        d=fixture();d['records'][0]['quotes'][0]['locator']={'section':'Results','paragraph':2};self.assertTrue(validate(d)['ok'])
    def test_abstract_only_cannot_be_full_extraction(self):
        d=fixture();d['records'][0]['access']='abstract';self.assertFalse(validate(d)['ok'])
    def test_retraction_cannot_support_core(self):
        d=fixture();d['records'][0]['integrity']['status']='retracted';self.assertFalse(validate(d)['ok'])
    def test_metric_without_provenance(self):
        d=fixture();d['records'][0]['metrics']=[{'name':'citation_count','entity':'work','value':100,'provider':'','observed_on':None,'source':None}];self.assertFalse(validate(d)['ok'])
    def test_true_zero_metric_allowed(self):
        d=fixture();d['records'][0]['metrics']=[{'name':'citation_count','entity':'work','value':0,'provider':'Synthetic provider','observed_on':'2026-09-10','source':'https://example.org/metric'}];self.assertTrue(validate(d)['ok'])
    def test_missing_metric_null_allowed(self):
        d=fixture();d['records'][0]['metrics']=[{'name':'journal_h_index','entity':'venue','value':None,'provider':'Unknown','observed_on':None,'source':None}];self.assertTrue(validate(d)['ok'])
    def test_wrong_metric_entity(self):
        d=fixture();d['records'][0]['metrics']=[{'name':'journal_h_index','entity':'author','value':None}];self.assertFalse(validate(d)['ok'])
    def test_publisher_claim_not_direct_index_evidence(self):
        d=fixture();d['manifest']['required_indexes']=['Scopus'];d['records'][0]['index_evidence']=[{'name':'Scopus','level':'publisher_claim','verified':True,'checked_on':'2026-09-10','source':'https://example.org/index'}];self.assertFalse(validate(d)['ok'])
    def test_verified_direct_index_evidence(self):
        d=fixture();d['manifest']['required_indexes']=['Scopus'];d['records'][0]['index_evidence']=[{'name':'Scopus','level':'direct_record','verified':True,'checked_on':'2026-09-10','source':'https://example.org/index'}];self.assertTrue(validate(d)['ok'])
    def test_unknown_claim_reference(self):
        d=fixture();d['claims'][0]['counter_ids']=['R9'];self.assertFalse(validate(d)['ok'])
    def test_same_study_family_warns(self):
        d=fixture();d['records'][0]['study_family']='S1';r=copy.deepcopy(d['records'][0]);r['id']='R2';d['records'].append(r);d['manifest']['reported_core']=2
        result=validate(d);self.assertTrue(result['ok']);self.assertIn('not independent',str(result['warnings']))
    def test_unverified_quote(self):
        d=fixture();d['records'][0]['quotes'][0]['verified']=False;self.assertFalse(validate(d)['ok'])
    def test_missing_required_quote(self):
        d=fixture();d['records'][0]['quotes']=[];self.assertFalse(validate(d)['ok'])
    def test_invalid_search_date(self):
        d=fixture();d['searches'][0]['date']='yesterday';self.assertFalse(validate(d)['ok'])
    def test_malformed_lists_report_errors(self):
        d=fixture();d['records'][0]['quotes']=None;self.assertFalse(validate(d)['ok'])
    def test_malformed_claim_references_report_errors(self):
        d=fixture();d['claims'][0]['support_ids']='R1';self.assertFalse(validate(d)['ok'])

if __name__=='__main__':unittest.main()
