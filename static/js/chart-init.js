var ctx = document.getElementById("lineChart").getContext("2d");
var gradient = ctx.createLinearGradient(0, 0, 0, 400);

// تعریف گرادیانت رنگ
gradient.addColorStop(0, "rgba(21, 99, 223,0.2)");
gradient.addColorStop(1, "rgba(21, 99, 223,0)");

var myChart = new Chart(ctx, {
  type: "line", // نوع نمودار خطی
  data: {
    labels: [
      "فروردین",
      "اردیبهشت",
      "خرداد",
      "تیر",
      "مرداد",
      "شهریور",
      "مهر",
      "آبان",
      "آذر",
      "دی",
      "بهمن",
      "اسفند",
    ],
    datasets: [
      {
        data: [
          42, 45, 70, 65, 140, 130, 145, 145, 160, 135, 140, 130, 135, 140, 250,
        ],
        backgroundColor: gradient,
        borderColor: "#1563DF",
        borderWidth: 2,
        fill: true, // رنگ زمینه
        tension: 0.4,
      },
    ],
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        display: false, // نمایش لیجن را غیرفعال کنید
      },
    },
    scales: {
      x: {
        reverse: true, // معکوس کردن برچسب‌های محور X برای راست‌چین شدن
        ticks: {
          font: {
            family: 'Peyda', // استفاده از فونت Peyda برای محور X
          },
        },
      },
      y: {
        beginAtZero: true,
        position: 'right', // جابجایی محور Y به سمت راست
        ticks: {
          font: {
            family: 'Peyda', // استفاده از فونت Peyda برای محور Y
          },
        },
      },
    },
    font: {
      family: 'Peyda', // تنظیم فونت کلی برای تمام نمودار
    },
  },
});
