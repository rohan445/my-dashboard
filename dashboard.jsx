import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line, Bar } from 'react-chartjs-2';
import { Form, Button, Row, Col, Container } from 'react-bootstrap';

function Dashboard() {
  const [data, setData] = useState([]);
  const [filters, setFilters] = useState({
    year: '',
    country: '',
    topics: '',
    region: '',
  });

  // Fetch Data from API
  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/api/data', { params: filters });
      setData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  // Trigger data fetch on filter changes
  useEffect(() => {
    fetchData();
  }, [filters]);

  // Update filters on change
  const handleFilterChange = (e) => {
    setFilters({
      ...filters,
      [e.target.name]: e.target.value,
    });
  };

  // Prepare chart data
  const lineChartData = {
    labels: data.map((item) => item.year),
    datasets: [
      {
        label: 'Intensity',
        data: data.map((item) => item.intensity),
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
        fill: true,
      },
    ],
  };

  const barChartData = {
    labels: data.map((item) => item.country),
    datasets: [
      {
        label: 'Likelihood',
        data: data.map((item) => item.likelihood),
        backgroundColor: 'rgba(255,99,132,0.6)',
      },
    ],
  };

  return (
    <Container>
      <h1 className="mt-4">Data Visualization Dashboard</h1>

      {/* Filter Form */}
      <Form className="my-4">
        <Row>
          <Col>
            <Form.Group controlId="filterYear">
              <Form.Label>Year</Form.Label>
              <Form.Control
                type="number"
                name="year"
                placeholder="Enter Year"
                onChange={handleFilterChange}
              />
            </Form.Group>
          </Col>

          <Col>
            <Form.Group controlId="filterCountry">
              <Form.Label>Country</Form.Label>
              <Form.Control
                type="text"
                name="country"
                placeholder="Enter Country"
                onChange={handleFilterChange}
              />
            </Form.Group>
          </Col>

          <Col>
            <Form.Group controlId="filterTopics">
              <Form.Label>Topics</Form.Label>
              <Form.Control
                type="text"
                name="topics"
                placeholder="Enter Topics"
                onChange={handleFilterChange}
              />
            </Form.Group>
          </Col>

          <Col>
            <Form.Group controlId="filterRegion">
              <Form.Label>Region</Form.Label>
              <Form.Control
                type="text"
                name="region"
                placeholder="Enter Region"
                onChange={handleFilterChange}
              />
            </Form.Group>
          </Col>
        </Row>
        <Button className="mt-3" onClick={fetchData}>
          Apply Filters
        </Button>
      </Form>

      {/* Data Visualizations */}
      <Row>
        <Col md={6} className="mb-4">
          <h5>Intensity Over Years</h5>
          <Line data={lineChartData} />
        </Col>

        <Col md={6} className="mb-4">
          <h5>Likelihood by Country</h5>
          <Bar data={barChartData} />
        </Col>
      </Row>
    </Container>
  );
}

export default Dashboard;
