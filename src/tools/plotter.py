"""
Plotter Tool - Generates charts from data.
Uses matplotlib to create bar/line/pie charts.
"""

import matplotlib.pyplot as plt
import pandas as pd
import base64
import io

class Plotter:
    """
    A tool to generate plots from data and return as base64 image.
    Supports bar, line, pie charts.
    """
    
    def run(self, data: dict, chart_type: str = "bar") -> str:
        """
        Generate a plot from data.
        Returns base64 encoded image for embedding in web/app.
        """
        try:
            df = pd.DataFrame(data)
            
            plt.figure(figsize=(8, 5))
            
            if chart_type == "bar":
                df.plot(kind="bar")
            elif chart_type == "line":
                df.plot(kind="line")
            elif chart_type == "pie":
                df.plot(kind="pie", autopct='%1.1f%%')
            else:
                return "Unsupported chart type. Use 'bar', 'line', or 'pie'."
            
            plt.title("Generated Chart")
            plt.ylabel("Value")
            plt.xticks(rotation=45)
            
            # Save to buffer
            buf = io.BytesIO()
            plt.savefig(buf, format="png", bbox_inches="tight")
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode("utf-8")
            plt.close()
            
            return f"![chart](data:image/png;base64,{img_base64})"
        except Exception as e:
            return f"Error generating plot: {str(e)}"

# Example
if __name__ == "__main__":
    plotter = Plotter()
    data = {"Month": ["Jan", "Feb", "Mar"], "Sales": [100, 150, 200]}
    print(plotter.run(data, "bar"))
