from ..request_utils import decode_json


def test_get_dataset(auth_client, ingest_neurosynth):
    # List of datasets
    resp = auth_client.get('/api/datasets')
    assert resp.status_code == 200
    dataset_list = decode_json(resp)
    assert type(dataset_list) == list