# tests/test_chirpstack_api.py

import unittest
from unittest.mock import patch, MagicMock
from jmq_chirpstack.chirpstack_api import JMQChirpstackAPI


class TestJMQChirpstackAPI(unittest.TestCase):
    def setUp(self):
        # Configuramos la instancia de la API para los tests
        self.base_url = "http://localhost:8080/api"
        self.api = JMQChirpstackAPI(base_url=self.base_url, api_key="fake_api_key")

    @patch("jmq_chirpstack.chirpstack_api.requests.get")
    def test_get_tenants(self, mock_get):
        # Definimos la respuesta esperada para tenants
        expected_response = [{"id": "tenant1", "name": "Tenant 1"}]

        # Configuramos el mock para simular una respuesta exitosa
        mock_resp = MagicMock()
        mock_resp.json.return_value = expected_response
        mock_resp.raise_for_status.return_value = None  # No lanza error
        mock_get.return_value = mock_resp

        tenants = self.api.get_tenants()
        # Verificar que se llamó a la URL correcta
        mock_get.assert_called_once_with(f"{self.base_url}/tenants", headers=self.api.headers)
        self.assertEqual(tenants, expected_response)

    @patch("jmq_chirpstack.chirpstack_api.requests.get")
    def test_get_gateways(self, mock_get):
        tenant_id = "tenant1"
        expected_response = [{"id": "gateway1", "name": "Gateway 1"}]

        mock_resp = MagicMock()
        mock_resp.json.return_value = expected_response
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        gateways = self.api.get_gateways(tenant_id)
        mock_get.assert_called_once_with(f"{self.base_url}/tenants/{tenant_id}/gateways", headers=self.api.headers)
        self.assertEqual(gateways, expected_response)

    @patch("jmq_chirpstack.chirpstack_api.requests.get")
    def test_get_sensors(self, mock_get):
        gateway_id = "gateway1"
        expected_response = [{"id": "sensor1", "type": "temperature"}]

        mock_resp = MagicMock()
        mock_resp.json.return_value = expected_response
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        sensors = self.api.get_sensors(gateway_id)
        mock_get.assert_called_once_with(f"{self.base_url}/gateways/{gateway_id}/sensors", headers=self.api.headers)
        self.assertEqual(sensors, expected_response)

    @patch("jmq_chirpstack.chirpstack_api.requests.get")
    def test_get_sensor_data(self, mock_get):
        sensor_id = "sensor1"
        start_time = "2022-01-01T00:00:00Z"
        end_time = "2022-01-02T00:00:00Z"
        expected_response = {"data": [1, 2, 3]}

        mock_resp = MagicMock()
        mock_resp.json.return_value = expected_response
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        data = self.api.get_sensor_data(sensor_id, start_time=start_time, end_time=end_time)
        mock_get.assert_called_once_with(
            f"{self.base_url}/sensors/{sensor_id}/data",
            headers=self.api.headers,
            params={"start": start_time, "end": end_time}
        )
        self.assertEqual(data, expected_response)


if __name__ == "__main__":
    unittest.main()
