import 'package:flutter/material.dart';
import 'package:table_calendar/table_calendar.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        brightness: Brightness.dark,
        primaryColor: const Color.fromARGB(255, 75, 61, 98).withOpacity(0.8), // Updated soft purple
        scaffoldBackgroundColor: const Color(0xFF121212), // Dark background
        appBarTheme: AppBarTheme(
          backgroundColor: const Color.fromARGB(255, 75, 61, 98).withOpacity(0.8), // Updated AppBar color
          titleTextStyle: const TextStyle(color: Colors.white), // Adjusted title color for contrast
        ),
        bottomNavigationBarTheme: const BottomNavigationBarThemeData(
          backgroundColor: Color(0xFF1E1E1E), // Darker bottom bar
          selectedItemColor: Color.fromARGB(255, 75, 61, 98), // Updated selected color
          unselectedItemColor: Colors.white70,
        ),
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _currentIndex = 0;
  final List<Widget> _pages = [
    const PainInputPage(),
    const PainChatPage(),
    const MedicalHistoryPage(),
    const PainPredictionPage(predictionData: []),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _pages[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.edit), label: 'Record Pain'),
          BottomNavigationBarItem(icon: Icon(Icons.chat), label: 'Chat'),
          BottomNavigationBarItem(icon: Icon(Icons.history), label: 'History'),
          BottomNavigationBarItem(icon: Icon(Icons.pie_chart), label: 'Predictions'),
        ],
      ),
    );
  }
}

class PainInputPage extends StatelessWidget {
  const PainInputPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Track Your Pain'),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            _buildSectionTitle("Pain Level"),
            _buildScrollableRow([
              _buildPainDescriptor(Icons.sentiment_very_dissatisfied, 'Severe', Colors.redAccent),
              _buildPainDescriptor(Icons.sentiment_dissatisfied, 'Moderate', Colors.deepOrangeAccent),
              _buildPainDescriptor(Icons.sentiment_neutral, 'Mild', Colors.amber),
              _buildPainDescriptor(Icons.sentiment_satisfied, 'None', Colors.greenAccent),
            ]),
            const SizedBox(height: 30),
            _buildSectionTitle("Pain Area"),
            _buildScrollableRow([
              _buildPainDescriptor(Icons.headset, 'Head', Colors.blueGrey),
              _buildPainDescriptor(Icons.accessibility_new, 'Back', Colors.purpleAccent),
              _buildPainDescriptor(Icons.directions_run, 'Leg', Colors.brown),
              _buildPainDescriptor(Icons.pan_tool, 'Hand', Colors.pinkAccent),
              _buildPainDescriptor(Icons.directions_walk, 'Foot', Colors.deepOrangeAccent),
              _buildPainDescriptor(Icons.healing, 'Stomach', Colors.green),
            ]),
            const SizedBox(height: 30),
            _buildSectionTitle("Energy Level"),
            _buildScrollableRow([
              _buildPainDescriptor(Icons.battery_full, 'Full', Colors.lightGreen),
              _buildPainDescriptor(Icons.battery_std, 'Moderate', Colors.amber),
              _buildPainDescriptor(Icons.battery_alert, 'Low', Colors.redAccent),
            ]),
            const SizedBox(height: 30),
            _buildSectionTitle("Mood"),
            _buildScrollableRow([
              _buildPainDescriptor(Icons.mood, 'Happy', Colors.lightGreen),
              _buildPainDescriptor(Icons.mood_bad, 'Sad', Colors.blueAccent),
              _buildPainDescriptor(Icons.sentiment_very_dissatisfied, 'Angry', Colors.redAccent),
            ]),
            const SizedBox(height: 30),
            Center(
              child: ElevatedButton(
                onPressed: () {
                  // Trigger backend pain recording
                },
                child: const Text('Submit Pain Information'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.grey[800], 
                  foregroundColor: Colors.white, 
                  padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 15),
                  textStyle: const TextStyle(fontSize: 16),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSectionTitle(String title) {
    return Text(
      title,
      style: const TextStyle(
        fontSize: 20,
        fontWeight: FontWeight.bold,
        color: Colors.white70,
      ),
    );
  }

  Widget _buildScrollableRow(List<Widget> items) {
    return SingleChildScrollView(
      scrollDirection: Axis.horizontal,
      child: Row(
        children: items.map((item) {
          return Padding(
            padding: const EdgeInsets.all(8.0),
            child: item,
          );
        }).toList(),
      ),
    );
  }

  Widget _buildPainDescriptor(IconData icon, String label, Color color) {
    return Container(
      padding: const EdgeInsets.all(16.0),
      decoration: BoxDecoration(
        color: Colors.grey[850],
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: color, width: 2),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.3),
            spreadRadius: 2,
            blurRadius: 5,
            offset: const Offset(0, 3),
          ),
        ],
      ),
      child: Column(
        children: [
          Icon(icon, size: 50, color: Colors.white),
          const SizedBox(height: 10),
          Text(
            label,
            style: const TextStyle(
              fontWeight: FontWeight.bold,
              color: Colors.white70,
            ),
          ),
        ],
      ),
    );
  }
}

// PainChatPage - Chat interface for pain suggestions
class PainChatPage extends StatefulWidget {
  const PainChatPage({super.key});

  @override
  _PainChatPageState createState() => _PainChatPageState();
}

class _PainChatPageState extends State<PainChatPage> {
  final TextEditingController _controller = TextEditingController();
  final List<Map<String, String>> _messages = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Pain Relief ChatBot'),
        backgroundColor: Color.fromARGB(255, 75, 61, 98),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(
                    _messages[index]['user']!,
                    style: const TextStyle(color:Color.fromARGB(255, 75, 61, 98)),
                  ),
                  subtitle: Text(
                    _messages[index]['bot']!,
                    style: const TextStyle(color: Colors.white),
                  ),
                );
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    style: const TextStyle(color: Colors.white), // Text input color
                    decoration: InputDecoration(
                      hintText: 'Ask for solutions...',
                      hintStyle: TextStyle(color: Colors.white.withOpacity(0.7)), // Hint text color
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10),
                        borderSide: const BorderSide(color: Colors.tealAccent),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderSide: BorderSide(color: Color.fromARGB(255, 75, 61, 98).withOpacity(0.7)),
                      ),
                    ),
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.send, color: Color.fromARGB(255, 75, 61, 98)),
                  onPressed: () {
                    setState(() {
                      _messages.add({
                        'user': _controller.text,
                        'bot': 'This is a suggestion based on the input.' // Mock response
                      });
                      _controller.clear();
                    });
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

// MedicalHistoryPage for tracking past pain and medical history
class MedicalHistoryPage extends StatefulWidget {
  const MedicalHistoryPage({super.key});

  @override
  _MedicalHistoryPageState createState() => _MedicalHistoryPageState();
}

class _MedicalHistoryPageState extends State<MedicalHistoryPage> {
  // Pain History Data
  final List<Map<String, dynamic>> historyData = [
    {'date': '2024-09-28', 'pain': 'Mild Pain'},
    {'date': '2024-09-27', 'pain': 'Severe Pain'},
    {'date': '2024-09-26', 'pain': 'Moderate Pain'},
  ];

  // Medical History Data
  final List<Map<String, dynamic>> medicalHistoryData = [
    {'title': 'Medical Diagnoses', 'details': 'Hypertension', 'icon': Icons.health_and_safety},
    {'title': 'Medical Operations', 'details': 'Appendectomy', 'icon': Icons.local_hospital},
    {'title': 'Allergies', 'details': 'Penicillin', 'icon': Icons.warning},
  ];

  // Calendar State
  DateTime _selectedDay = DateTime.now();
  DateTime _focusedDay = DateTime.now();
  late Map<DateTime, List<String>> _events;

  @override
  void initState() {
    super.initState();
    _events = _createPainHistoryEvents();
  }

  // Helper function to create event map from pain history
  Map<DateTime, List<String>> _createPainHistoryEvents() {
    Map<DateTime, List<String>> events = {};
    for (var entry in historyData) {
      DateTime date = DateTime.parse(entry['date']);
      String painLevel = entry['pain'];
      if (events.containsKey(date)) {
        events[date]!.add(painLevel);
      } else {
        events[date] = [painLevel];
      }
    }
    return events;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Medical History'),
        backgroundColor:Color.fromARGB(255, 50, 40, 66),
        centerTitle: true,
      ),
      body: Column(
        children: [
          _buildCalendarView(),
          const SizedBox(height: 10),
          _buildSectionTitle('Pain History', Icons.healing),
          _buildPainHistoryList(),
          const SizedBox(height: 20),
          _buildSectionTitle('Medical History', Icons.medical_services),
          const SizedBox(height: 10),
          _buildMedicalHistoryList(),
        ],
      ),
    );
  }

  // Calendar widget based on TableCalendar
  Widget _buildCalendarView() {
    return Card(
      margin: const EdgeInsets.all(8.0), // Add margin around the calendar for spacing
      elevation: 3,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
      child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: TableCalendar(
          firstDay: DateTime.utc(2020, 1, 1),
          lastDay: DateTime.utc(2030, 12, 31),
          focusedDay: _focusedDay,
          selectedDayPredicate: (day) => isSameDay(_selectedDay, day),
          onDaySelected: (selectedDay, focusedDay) {
            setState(() {
              _selectedDay = selectedDay;
              _focusedDay = focusedDay;
            });
          },
          eventLoader: (day) {
            return _events[day] ?? [];
          },
          startingDayOfWeek: StartingDayOfWeek.sunday,
          calendarStyle: CalendarStyle(
            todayDecoration: BoxDecoration(
              color: Color.fromARGB(255, 75, 61, 98),
              shape: BoxShape.circle,
            ),
            selectedDecoration: BoxDecoration(
              color:Color.fromARGB(255, 75, 61, 98),
              shape: BoxShape.circle,
            ),
            markerDecoration: BoxDecoration(
              color: Colors.redAccent[200],  // Pink markers for events
              shape: BoxShape.circle,
            ),
            outsideDaysVisible: false,
            weekendTextStyle: TextStyle(
              color: Theme.of(context).brightness == Brightness.dark ? Colors.red[300] : Colors.red[600],
            ),
          ),
          headerStyle: const HeaderStyle(
            formatButtonVisible: false,
            titleCentered: true,
            headerPadding: EdgeInsets.all(8.0),
          ),
          daysOfWeekStyle: DaysOfWeekStyle(
            weekendStyle: TextStyle(
              color: Theme.of(context).brightness == Brightness.dark ? Colors.red[300] : Colors.red,
            ),
          ),
        ),
      ),
    );
  }

  // Pain History List with icons and colors
  Widget _buildPainHistoryList() {
    return Expanded(
      child: ListView.builder(
        itemCount: historyData.length,
        itemBuilder: (context, index) {
          return Card(
            margin: const EdgeInsets.symmetric(vertical: 5, horizontal: 15),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(10),
            ),
            elevation: 2,
            color: Colors.grey[850], // Dark card color for history
            child: ListTile(
              leading: const Icon(
                Icons.history,
                color: Color.fromARGB(255, 75, 61, 98),
              ),
              title: Text(
                'Date: ${historyData[index]['date']}',
                style: const TextStyle(fontWeight: FontWeight.bold, color:Color.fromARGB(255, 221, 221, 221)),
              ),
              subtitle: Text(
                'Pain Level: ${historyData[index]['pain']}',
                style: const TextStyle(color: Colors.white),
              ),
              trailing: Icon(
                Icons.warning_amber_rounded,
                color: _getPainIconColor(historyData[index]['pain']),
              ),
            ),
          );
        },
      ),
    );
  }

  // Get color for pain level icon based on severity
  Color _getPainIconColor(String painLevel) {
    switch (painLevel) {
      case 'Severe Pain':
        return Colors.redAccent;
      case 'Moderate Pain':
        return Colors.amber;
      case 'Mild Pain':
        return Colors.greenAccent;
      default:
        return Colors.grey;
    }
  }

  // Medical history list with better styling
  Widget _buildMedicalHistoryList() {
    return Expanded(
      child: ListView.builder(
        itemCount: medicalHistoryData.length,
        itemBuilder: (context, index) {
          return Card(
            margin: const EdgeInsets.symmetric(vertical: 5, horizontal: 15),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(10),
            ),
            elevation: 2,
            color: Colors.grey[850], // Dark card color for history
            child: ListTile(
              leading: Icon(
                medicalHistoryData[index]['icon'],
                color: Color.fromARGB(255, 75, 61, 98),
              ),
              title: Text(
                medicalHistoryData[index]['title'],
                style: const TextStyle(fontWeight: FontWeight.bold, color: Color.fromARGB(255, 233, 233, 233)),
              ),
              subtitle: Text(
                medicalHistoryData[index]['details'],
                style: const TextStyle(color: Colors.white),
              ),
            ),
          );
        },
      ),
    );
  }

  // Section title with icon
  Widget _buildSectionTitle(String title, IconData icon) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 15),
      child: Row(
        children: [
          Icon(icon, color: Color.fromARGB(255, 108, 88, 141)),
          const SizedBox(width: 8),
          Text(
            title,
            style: const TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
              color:Color.fromARGB(255, 92, 73, 122),
            ),
          ),
        ],
      ),
    );
  }
}

// PainPredictionPage - Future pain predictions visualization
class PainPredictionPage extends StatefulWidget {
  final List<Map<String, dynamic>> predictionData;

  const PainPredictionPage({super.key, required this.predictionData});

  @override
  _PainPredictionPageState createState() => _PainPredictionPageState();
}

class _PainPredictionPageState extends State<PainPredictionPage> {
  late ScrollController _scrollController;

  @override
  void initState() {
    super.initState();
    _scrollController = ScrollController();
  }

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Pain Prediction'),
        backgroundColor: const Color.fromARGB(255, 75, 61, 98).withOpacity(0.8),
        elevation: 0,
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [Colors.black, Colors.grey[850]!],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
        ),
        padding: const EdgeInsets.all(20.0),
        child: SingleChildScrollView(
          controller: _scrollController,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                'Predicted Pain Levels',
                style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Colors.white),
              ),
              const SizedBox(height: 20),

              // Placeholder for the graph
              Container(
                height: 250, // Placeholder height for the graph
                width: double.infinity,
                decoration: BoxDecoration(
                  color: Colors.grey[800],
                  borderRadius: BorderRadius.circular(12),
                  boxShadow: const [
                    BoxShadow(color: Colors.black26, blurRadius: 10, spreadRadius: 2),
                  ],
                ),
                child: const Center(
                  child: Text(
                    'Graph Placeholder',
                    style: TextStyle(color: Colors.white, fontSize: 20),
                  ),
                ),
              ),
              const SizedBox(height: 20),

              // Hourly Pain Levels
              const Text(
                'Hourly Pain Predictions',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.w600, color: Colors.white),
              ),
              const SizedBox(height: 10),

              // Creating a list of hourly predictions
              Wrap(
                spacing: 15,
                runSpacing: 15,
                children: List.generate(24, (index) {
                  return HourItem(index: index);
                }),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

// HourItem widget to represent each hourly pain prediction
class HourItem extends StatelessWidget {
  final int index;

  const HourItem({super.key, required this.index});

  @override
  Widget build(BuildContext context) {
    Color borderColor;
    IconData icon;
    String hour = '${index % 12 == 0 ? 12 : index % 12} ${index < 12 ? 'AM' : 'PM'}';
    int painLevel = (index % 5) + 1;

    switch (painLevel) {
      case 1:
        borderColor = Colors.green; // Light green for level 1
        icon = Icons.sentiment_satisfied;
        break;
      case 2:
        borderColor = Colors.lightGreen; // Slightly darker green for level 2
        icon = Icons.sentiment_satisfied;
        break;
      case 3:
        borderColor = Colors.orange; // Orange for level 3
        icon = Icons.sentiment_neutral;
        break;
      case 4:
        borderColor = Colors.deepOrange; // Darker orange for level 4
        icon = Icons.sentiment_dissatisfied;
        break;
      case 5:
        borderColor = Colors.red; // Red for level 5
        icon = Icons.sentiment_very_dissatisfied;
        break;
      default:
        borderColor = Colors.grey; // Default color
        icon = Icons.help;
    }

    return Container(
      width: 100, // Fixed width for uniformity
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.grey[800], // Darker background color for the item
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: borderColor, width: 2), // Colored border
        boxShadow: const [
          BoxShadow(color: Colors.black26, blurRadius: 10, spreadRadius: 2),
        ],
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, size: 40, color: Colors.white),
          const SizedBox(height: 8),
          Text(
            hour,
            style: const TextStyle(
              color: Colors.white,
              fontSize: 16,
              fontWeight: FontWeight.w500,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            'Pain Level: $painLevel', // Show the pain level with prefix
            style: const TextStyle(
              color: Colors.white,
              fontSize: 14,
              fontWeight: FontWeight.w400,
            ),
          ),
        ],
      ),
    );
  }
}
