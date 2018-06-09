import pytest

from indy_common.req_utils import get_write_claim_def_signature_type, \
    get_write_claim_def_schema_ref, get_write_claim_def_tag, get_write_claim_def_public_keys, \
    get_read_claim_def_signature_type, get_read_claim_def_schema_ref, get_read_claim_def_tag, get_read_claim_def_from
from indy_common.types import SafeRequest


@pytest.fixture(scope="module", params=['dict', 'Request'])
def write_claim_def_request(request):
    req = {
        'operation': {
            'type': '102',
            'signature_type': 'CL',
            'ref': 18,
            'tag': 'key111',
            'data': {
                'primary': {'primaryKey1': 'a'},
                'revocation': {'revocationKey1': 'b'}
            },
        },

        'identifier': 'L5AD5g65TDQr1PPHHRoiGf',
        'reqId': 1514280215504647,
        'protocolVersion': 1,
        'signature': '5ZTp9g4SP6t73rH2s8zgmtqdXyTuSMWwkLvfV1FD6ddHCpwTY5SAsp8YmLWnTgDnPXfJue3vJBWjy89bSHvyMSdS'
    }
    if request.param == 'dict':
        return req
    return SafeRequest(**req)


@pytest.fixture(scope="module")
def read_claim_def_request():
    req = {
        'operation': {
            'type': '108',
            'signature_type': 'CL',
            'ref': 18,
            'tag': 'key111',
            'origin': 'L5AD5g65TDQr1PPHHRoiGf'
        },

        'identifier': 'E5AD5g65TDQr1PPHHRoiGf',
        'reqId': 1514280215504647,
        'protocolVersion': 1
    }
    return SafeRequest(**req)


def test_get_write_claim_def_signature_type(write_claim_def_request):
    assert 'CL' == get_write_claim_def_signature_type(write_claim_def_request)


def test_get_write_claim_def_schema_ref(write_claim_def_request):
    assert 18 == get_write_claim_def_schema_ref(write_claim_def_request)


def test_get_write_claim_def_tag(write_claim_def_request):
    assert 'key111' == get_write_claim_def_tag(write_claim_def_request)


def test_get_write_claim_public_keys(write_claim_def_request):
    assert {'primary': {'primaryKey1': 'a'}, 'revocation': {'revocationKey1': 'b'}} == \
           get_write_claim_def_public_keys(write_claim_def_request)


def test_get_read_claim_def_signature_type(read_claim_def_request):
    assert 'CL' == get_read_claim_def_signature_type(read_claim_def_request)


def test_get_read_claim_def_schema_ref(read_claim_def_request):
    assert 18 == get_read_claim_def_schema_ref(read_claim_def_request)


def test_get_read_claim_def_tag(read_claim_def_request):
    assert 'key111' == get_read_claim_def_tag(read_claim_def_request)


def test_get_read_claim_def_from(read_claim_def_request):
    assert 'L5AD5g65TDQr1PPHHRoiGf' == get_read_claim_def_from(read_claim_def_request)