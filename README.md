# Q1 2024 Sales Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange)](https://pandas.pydata.org/)
[![React](https://img.shields.io/badge/React-18%2B-61DAFB)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive sales data analysis project featuring Python-based data processing and an interactive React dashboard for visualizing Q1 2024 sales performance.



## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Analysis](#data-analysis)
- [Dashboard](#dashboard)
- [Key Insights](#key-insights)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a complete sales analysis solution for Q1 2024 (January-March) including:

- **Data Generation**: Realistic sample sales data with 5,000+ records
- **Data Processing**: Python-based cleaning, transformation, and analysis
- **Visualizations**: 8+ charts covering trends, categories, regions, and customers
- **Interactive Dashboard**: React-based web application with tabbed navigation
- **Business Insights**: Actionable recommendations based on data analysis

### Key Metrics Summary

| Metric | Value |
|--------|-------|
| Total Revenue | $4,070,016.31 |
| Total Orders | 5,000 |
| Unique Customers | 1,180 |
| Average Order Value | $814.00 |
| Customer Lifetime Value | $3,449.17 |
| Repeat Customer Rate | 94.07% |

## Features

### Data Analysis
- Monthly sales trend analysis with growth calculations
- Product category performance breakdown
- Regional sales comparison across 4 regions
- Customer segmentation (VIP, High Value, Medium Value, Low Value, New)
- Purchase frequency and behavior analysis
- Key Performance Indicators (KPIs) calculation

### Dashboard
- **6 Navigation Tabs**: Overview, Trends, Categories, Regions, Customers, Insights
- **Interactive Charts**: Bar charts, pie charts, line charts with hover tooltips
- **KPI Cards**: Visual summary of key metrics with gradient styling
- **Data Tables**: Formatted tables with currency and number formatting
- **Responsive Design**: Works on desktop and mobile devices

### Visualizations
1. Monthly revenue comparison
2. Daily revenue trends
3. Product category distribution (pie chart)
4. Category revenue breakdown (horizontal bar)
5. Regional performance comparison
6. Market share by region
7. Customer segmentation
8. Order value distribution

## Project Structure

```
sales-analysis-dashboard/
├── data/
│   └── sales_data_q1_2024.csv          # Sample sales dataset
├── scripts/
│   ├── generate_sample_data.py         # Data generation script
│   └── sales_analysis_report.py        # Main analysis script
├── dashboard/
│   └── index.html                      # React dashboard (single file)
├── outputs/
│   ├── chart_monthly_revenue.png       # Generated visualizations
│   ├── chart_category_distribution.png
│   ├── chart_regional_performance.png
│   └── ...
├── README.md                           # This file
└── requirements.txt                    # Python dependencies
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Python Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

### Dashboard

The dashboard is a self-contained HTML file with no build step required. Simply open `dashboard/index.html` in your browser.

## Usage

### 1. Generate Sample Data

```bash
python scripts/generate_sample_data.py
```

This creates `data/sales_data_q1_2024.csv` with 5,000 realistic sales records.

### 2. Run Analysis

```bash
python scripts/sales_analysis_report.py
```

This will:
- Load and clean the sales data
- Calculate KPIs and metrics
- Generate visualizations (saved to `outputs/`)
- Create an HTML report (`outputs/sales_analysis_report_q1_2024.html`)

### 3. View Dashboard

Open `dashboard/index.html` in your web browser:

```bash
# macOS
open dashboard/index.html

# Linux
xdg-open dashboard/index.html

# Windows
start dashboard/index.html
```

Or serve it locally:

```bash
cd dashboard
python -m http.server 8000
# Then visit http://localhost:8000
```

## Data Analysis

### Data Schema

| Column | Type | Description |
|--------|------|-------------|
| order_id | string | Unique order identifier |
| order_date | date | Date of purchase |
| order_month | int | Month (1-3) |
| customer_id | string | Unique customer identifier |
| region | string | Geographic region (North, South, East, West) |
| product_category | string | Product category (7 categories) |
| product_name | string | Specific product name |
| quantity | int | Units purchased |
| unit_price | float | Price per unit |
| total_amount | float | Gross order amount |
| discount | float | Discount applied |
| final_amount | float | Net order amount |

### Analysis Workflow

1. **Data Loading**: Import CSV and validate structure
2. **Data Cleaning**: Check for missing values, duplicates, outliers
3. **KPI Calculation**: Compute revenue, orders, AOV, CLV metrics
4. **Trend Analysis**: Monthly aggregation and growth calculations
5. **Category Analysis**: Revenue breakdown by product category
6. **Regional Analysis**: Performance comparison across regions
7. **Customer Analysis**: Segmentation and behavior analysis
8. **Visualization**: Generate charts and export to HTML

## Dashboard

### Navigation

The dashboard is organized into 6 tabs:

#### Overview
- 4 KPI cards (Revenue, Orders, Customers, AOV)
- Additional metrics table
- Quick charts for monthly revenue and category distribution

#### Monthly Trends
- Monthly performance summary table
- Revenue vs Orders comparison chart
- Average Order Value trend line chart

#### Categories
- Revenue distribution pie chart
- Category revenue bar chart
- Detailed category performance table

#### Regions
- Revenue by region bar chart
- Market share pie chart
- Regional performance metrics table

#### Customers
- Customer segment distribution
- Revenue by segment analysis
- Detailed segment metrics table

#### Insights
- Key findings cards with icons
- Business recommendations
- Strategic action items

### Customization

To use your own data:

1. Replace `data/sales_data_q1_2024.csv` with your dataset
2. Update the column names in `sales_analysis_report.py` if needed
3. Re-run the analysis script
4. Update the data object in `dashboard/index.html` (lines 30-90)

## Key Insights

### Top Findings

1. **Best Performing Month**: March generated $1.40M in revenue (5.5% growth from February)

2. **Top Product Category**: Electronics dominates with $2.56M (63% of total revenue)

3. **Leading Region**: East region contributed $1.26M with the highest AOV of $946.66

4. **VIP Customer Impact**: 118 VIP customers generated $1.24M, averaging $10,467 per customer

5. **Customer Loyalty**: 94.07% repeat customer rate indicates strong retention

### Business Recommendations

1. **Focus on High-Value Categories**: Expand Electronics and Home & Garden product variety
2. **Optimize Regional Strategies**: Apply East/North tactics to South/West regions
3. **Nurture VIP Customers**: Implement loyalty programs and exclusive offers
4. **Increase Purchase Frequency**: Use email marketing to drive repeat purchases
5. **Monitor Seasonal Trends**: Optimize inventory and staffing based on patterns
6. **Review Discount Strategy**: Evaluate if strategic discounts could drive volume

## Technologies Used

### Data Analysis
- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Static visualizations
- **Seaborn**: Statistical data visualization

### Dashboard
- **React 18**: UI library
- **Tailwind CSS**: Utility-first CSS framework
- **Recharts**: Composable charting library
- **Babel**: JavaScript compiler (in-browser)

### Development
- **Git**: Version control
- **GitHub**: Repository hosting

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution

- Additional visualizations
- More data analysis features
- Dashboard UI improvements
- Documentation updates
- Bug fixes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Sample data generated for demonstration purposes
- Charts powered by [Recharts](https://recharts.org/)
- Styling with [Tailwind CSS](https://tailwindcss.com/)

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: This project uses sample data for demonstration. Replace with your actual sales data for production use.
